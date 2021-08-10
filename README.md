# CloudKey-Display-Script
![Display](https://github.com/dgoumans/CloudKey-Display-Script/blob/main/display.png?raw=true)

## SSH onto cloudkey

    apt-get install python3-pip
    python3 -m pip install --upgrade pip
    python3 -m pip install --upgrade Pillow

run display.py every minute to generate and use the new image using crontab (using the `crontab -e `command)

    * * * * * python3 ~/display.py
    * * * * * /sbin/ck-splash -f display.png

and now kill the Unifi service that keeps grabbing the UI (this will relaunch on reboot)

    lsof /dev/fb0
    kill <id>

Now every minute the display should update with the time

