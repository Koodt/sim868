# sim868
Raspberry PI 3B Plus, GPS/GNSS/GSM/GPRS hat for smart home / package receiver / mongodb

# Enable GPIO UART
Add to /boot/config.txt string:

enable_uart=1

# Disable login prompt on serial port

sudo raspi-config

> Interfacing Options
> P6 Serial
> Would you like a login shell to be accessible over serial? No
> Would you like the serial port hardware to be enabled? Yes

# Requierements
pyserial
