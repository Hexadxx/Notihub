# Notihub

## Technologies used

- Debian 11
- Digital Oceans
- Python 3
- Django
- MQTT




## Settings instructions
The server is hosted on an instance in DigitalOcean cloud. 

Follow this tutorial for the initial setup of our server: [Initial Server Setup with Debian 11](https://www.digitalocean.com/community/tutorials/initial-server-setup-with-debian-11)


## Guide for setting up the dashboard
1. Create a directory where you want to set up Notihub
2. Create a virtual env 
    >virtualenv --system-site-packages -p python3 env/

    if you don't have virtualenv install, you can install it with the following command 

    >sudo apt-get -y install virtualenv
3. Install the programs using pip with the requirements.txt
    >pip3 install -r requirements.txt
4. Edit /core/settings.py. Edit the lines `ALLOWED_HOSTS` and `CSRF_TRUSTED_ORIGINS` to add your IP or domain
5. To run the server
    >Python3 manage.py runserver 0.0.0.0:8000

## Guide for setting up the MQTT broker
### Installation
1. Update and refresh your Debian package via the following command
    >sudo apt update
2. Search for Mosquitto MQTT broker
    >sudo apt search mosquitto
3. Install the following Mosquitto package
    >sudo apt install mosquitto mosquitto-clients
4. After the installation, check if the Mosquitto service is working
    >sudo systemctl is-enabled mosquitto

    You should get the following response: _enabled_
    >sudo systemctl status mosquitto

    You should get a response which includes: _active (running)_
### Setting up authentication
1. Create a user and password
    >sudo mosquitto_passwd -c /etc/mosquitto/.passwd username
2. Use your favorite text editor to open the file auth.conf
    >sudo micro /etc/mosquitto/conf.d/auth.conf
3. Add the following configration t o disable anonymous access and define the password file
    >allow_anonymous false
    password_file /etc/mosquitto/.passwd
    
    Save  the file and exit your editor (PS: we hope that you're using micro) when you're finished
    >sudo systemctl restart mosquitto
4. Edit /core/settings.py. Edit the lines `MQTT_USER ` and `MQTT_USER ` to add the user and password you just created
You should have someting like this
    `MQTT_SERVER = 'localhost'`

    `MQTT_PORT = 1883`

    `MQTT_KEEPALIVE = 60`

    `MQTT_USER = 'username'`

    `MQTT_PASSWORD = 'thisIsAVerySecuredPassword'`
5. Setup the firewall to accept MQTT requests that use the port 1883 by default
    >sudo ufw allow 1883

    Check it with the following command:
    >sudo ufw status

    you should have this line in your table

    
    | To | Action | From |
    | ----------- | ----------- | ----------- |
    |`8000 (v6)` | `ALLOW`      | `Anywhere (v6)` 

6. For the change to apply you need to restart the MQQT broker service

## Guide for setting up the Django database


## Version used

| Name | Version |
| ----------- | ----------- |
| Debian | 11 (bullseye) |
| Django | 3.2.13 |
| Python | 3.9.2 |
| Mosquitto | 2.0.15|
| Paho-mqtt | 1.6.1 |
| MQTT | 3.9.2 |


### Notihub © Made with ❤️ by Eetu and Sébastien | December 2022 | Haaga-Helia

![Logo Notihub](./docs/Notihub_logo.png "Notihub logo")
![Logo Haaga-Helia](./docs/HH_logo.png "Haaga-Helia logo")
 