#!/bin/bash

# Sprawdzenie czy skrypt jest wykonywany z uprawnieniami roota
if [ "$EUID" -ne 0 ]
  then echo "Ten skrypt musi być uruchomiony z uprawnieniami roota"
  exit
fi

# Uruchomienie agenta Bluetooth
bluetoothctl << EOF
agent on
EOF

# Włączenie widoczności Bluetooth przez 60 sekund
bluetoothctl << EOF
discoverable on
pairable on
timeout 60
EOF

# Pobranie adresu MAC kontrolera PS3
echo "Naciśnij przycisk PS na kontrolerze PS3, a następnie naciśnij Enter"
read
echo "Oczekiwanie na połączenie z kontrolerem PS3..."
PS3_MAC=$(hcitool scan | grep "PLAYSTATION(R)3 Controller" | awk '{print $1}')

# Sprawdzenie czy adres MAC został pobrany poprawnie
if [ -z "$PS3_MAC" ]
  then echo "Nie udało się pobrać adresu MAC kontrolera PS3"
  exit
fi

# Parowanie z kontrolerem PS3
bluetoothctl << EOF
pair $PS3_MAC
connect $PS3_MAC
EOF

# Ustawienie właściwości protokołu HID
echo "Ustawianie właściwości protokołu HID..."
hidclient -l | grep "PLAYSTATION(R)3 Controller" | awk '{print $2}' | xargs -I {} hidclient -e {} 1

# Sprawdzenie czy połączenie jest już zestawione
if [ "$(bluetoothctl info $PS3_MAC | grep "Connected: yes")" == "Connected: yes" ]
  then echo "Kontroler PS3 jest już sparowany i połączony"
  exit
fi

# Wyłączenie widoczności Bluetooth
bluetoothctl << EOF
discoverable off
pairable off
EOF

echo "Sparowanie i konfiguracja kontrolera PS3 zostały zakończone"