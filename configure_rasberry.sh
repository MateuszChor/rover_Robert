# run with  yes | ./configure_rasberry.sh for auto yes on all question for install dependensies

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
pair 00:1A:7D:DA:71:11
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

# tool for handle ps3 events
sudo apt-get install python3-evdev

# for camera websocket
sudo apt install v4l-utils
sudo apt-get install libopenjp2-7-dev
sudo apt-get install libatlas-base-dev
sudo apt-get install libhdf5-dev
sudo apt-get install python3-h5py
sudo apt-get install python3-opencv
sudo apt install remoteit


# sudo apt-get install libjasper-dev
# sudo apt-get install libqtgui4
# sudo apt-get install libqt4-test



# PYTHON dependencies
sudo pip3 install flask
sudo pip3 install numpy
sudo pip3 install picamera
sudo pip3 install opencv-contrib-python
sudo pip3 install imutils
sudo pip3 install opencv-python



# sudo apt-get install aptitude
# sudo apt-get install python3-picamera python-picamera
# sudo apt-get install libraspberrypi0 libraspberrypi-bin libraspberrypi-dev
# sudo ldconfig
