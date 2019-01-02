# OpenHAB Configuration
#### Student Name: *Richard Whitney*   Student ID: *20040645*

These are all the files needed to get the openHAB installation up and running. 
A lot of them are generated during installation.

#### The files that I worked on are in the following folders:

#### items
 - devices.items
 - lights.items
 - sensores.items
 - time.items

#### rules
 - main.rules
  - I didn't get a chance to show the "sunrise" and "sunset" rules in the demo video. They turn on/off the lights during the day
 
#### scripts
 - client_pub.py
  - This is where I publish the senseHat data using mqtt.
 
#### services
 - addons.cfg
  - installs the required bindings

 - mqtt.cfg
  - Sets up the MQTT broker
 
#### sitemaps
 - default.sitemap
  - UI layout
  
#### Additional libraries required

##### samsungctl

###### Installation
    # pip install samsungctl

https://github.com/Ape/samsungctl

##### ps4-waker

###### Installation
[![NPM](https://nodei.co/npm/ps4-waker.png?mini=true)](https://nodei.co/npm/ps4-waker/)

https://github.com/dhleong/ps4-waker
 
## Project Demo
https://youtu.be/gUP8QXdc91Y

## Project Repo
https://github.com/richardwhitney/openhab-entertainment-room
