# CrackiGotchi
![](images/crackigotchi.gif)


# Materials
* [Raspberry Pi Zero WH](https://amzn.to/49mZVxC)<br />
* [Raspberry Pi Zero 2 WH](https://amzn.to/3VO7eu2)<br />
* [Micro SD Cards](https://amzn.to/4erXgWD)<br />
* [2.13-inch e-ink Waveshare 4 display](https://amzn.to/3HTGT6h)<br />
* [2.23inch OLED HAT](https://amzn.to/3V2gCKb)<br />
* [Battery pack](https://amzn.to/4e2aQzL)<br />
* [90-degree GPIO extenders & splitter](https://amzn.to/3Uooea9)<br />
* [Stand-off brackets](https://amzn.to/3St6NSX)<br />
<br />
_(Amazon affiliate links)_<br />

_[WATCH THE BUILD](https://www.reddit.com/u/froggyCaller/s/En8RwPh16d)_


## **Installations**

1. **OS install:**
   - Raspberry Pi Zero WH - [Pwnagotchi](https://pwnagotchi.ai/installation/) <br />
   - Raspberry Pi Zero 2 WH - Pi OS Lite 64-bit

2. **Enable SPI & I2C:**
   - Open a terminal on your Raspberry Pi.
   - Run sudo raspi-config.
   - Navigate to Interfacing Options -> SPI -> Enable.
   - Navigate to Interfacing Options -> I2C -> Enable.

   <br />

# Wiring and Setup
1. **Connecting the OLED HAT to Raspberry Pi:**
   - Use the 90-degree GPIO extenders to connect the OLED HAT to the Raspberry Pi. This provides a better viewing angle for the display. <br />

2. **Powering the Pi:**
   - If using a Pi Zero 2 W, connect the UPS Hat for continuous power supply. This will allow you to move the project anywhere without worrying about power interruptions.
  

# Usage Instructions
1. SSH Access:
   - You can also access your Raspberry Pi remotely using SSH. Use the following command to connect:
   - ssh pi@<your_pi_ip_address>
   
2. Display Message:
   - Once logged in, navigate to the project directory and run the python script display.
     
     ```
     python3 password.py
     ```
     Note: password.py does not actually crack any passwords. It only shows random passwords from rockyou.txt or randomly generated characters.

# Troubleshooting
1. Common Issues:
   - Ensure SPI & I2C are enabled in the Raspberry Pi configuration.
   - Check all connections if the screen does not display anything.
   - Verify all required packages are installed correctly.
   - [More Info](https://www.waveshare.com/wiki/2.23inch_OLED_HAT)
<br />
