sudo apt update
sudo apt upgrade

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
scan on
pair 00:1A:7D:DA:71:11
scan off
exit
EOF

if [ $? -eq 0 ]; then
    echo "Find and add ps3 pad ."
else
    echo "Error bad ps3 mac address or "


# list all connected device 
ls /dev/input

# # for test 
# cat /dev/input/event1



# PYTHON dependecies
# tool for handle ps3 events
sudo apt-get install python3-evdev

