# Important Information
THIS ONLY WORKS FOR **SH1106 I2C DISPLAYS** FOR NOW.

It was made on a 128x64 1.3" display and therefore is optimized for that display size

(I have a standard SSD1306 I2C here so i might make it compatible with that one too)

# Installation Steps
This installation is based on the bare belabox image
## 1. Get Git
```shell
sudo apt update
sudo apt install git python3-pip i2c-tools python3.8
```
## 2. Checkout project and test-run display
```shell
git clone https://github.com/isntfunny/belabox-i2c-display.git
cd belabox-i2c-display
python3.8 -m venv ./venv/
source ./venv/bin/activate
python3.8 -m pip install --upgrade pip setuptools wheel
python3.8 -m pip install -r requirements.txt
python3.8 main.py
```
If everything works, continue. If not, debug

## 3. Install as a service
COMING REAL SOON™

# Updating
```shell
cd belabox-i2c-display && git pull
```