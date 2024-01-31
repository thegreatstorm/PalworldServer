# PalWorld Dedicated Server

<img src="https://cdn.akamai.steamstatic.com/steam/apps/1623730/header.jpg" alt="My cool logo"/>

## Credit RCON functionality to following
https://github.com/gavinnn101/palworld_dedi_helper
https://github.com/eternity336/PalworldServerMonitor

## Summary
This python application was design to help installing and running palworld dedicated servers
you can even run rcon using this python application! 

## Commands
```angular2html
  -h, --help  show this help message and exit
  --install   Install Palworld Server
  --start     Run Palworld Server
  --stop      Stop Palworld Server
  --check     Check Running
  --clean     Destroys server folder
  --restart   Restart Palworld Server
  --rcon      Rcon Connect To Palworld Server
```

## Prerequisites
* Ubuntu Latest 64-bit
    * `dpkg --add-architecture i386; apt update; apt install lib32gcc-s1 steamcmd ansible wget tar unzip git python3.11 vim netcat pip `
    
## Recommended Setup: 
### Set a default user
```USER gameadmin```

### Set the working directory
```Working Directory: /home/gameadmin/```

### Setup and install steamcmd steamclient.so
```angular2html
mkdir -p /home/gameadmin/.steam/sdk64/
/usr/games/steamcmd +login anonymous +app_update 1007 +quit
cp /home/gameadmin/Steam/steamapps/common/Steamworks\ SDK\ Redist/linux64/steamclient.so /home/gameadmin/.steam/sdk64/
echo "alias steamcmd=\"/usr/games/steamcmd\"" >> /home/gameadmin/.bashrc
```

### Notes
You will get one error steamclient.so, but the server is running. If its more than one error than you may have issues with steamclient.so.