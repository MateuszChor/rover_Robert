sudo apt update
sudo apt upgrade

# for temperature check from terminal type sensors to check cpu temp
sudo apt install lm-sensors
sudo sensors-detect
# sudo systemctl restart kmod


# ps3 detect address with usb cable
sudo apt install libusb-dev
mkdir ~/sixpair
cd ~/sixpair
wget http://www.pabr.org/sixlinux/sixpair.c
gcc -o sixpair sixpair.c -lusb
sudo ~/sixpair/sixpair

# bluetooth 
sudo apt-get install bluetooth bluez blueman
sudo bluetoothctl <<EOF
agent on
default-agent
mac_address=$(scan on)
# pair 00:1A:7D:DA:71:11
pair mac_address
scan off
exit
EOF

if [ $? -eq 0 ]; then
    echo "Find and add ps3 pad ."
else
    echo "Error bad ps3 mac address or "
fi

# list all connected device 
ls /dev/input
# cat /dev/input/event1

# PYTHON dependencies
# tool for handle ps3 events
sudo apt-get install python3-evdev