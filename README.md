<p align="center">
<img align="center" src="https://user-images.githubusercontent.com/30548669/215224890-e3848de4-342e-49a7-ac43-a27e1af08584.png" width="70%"/>
</p>


# SaiUnes Streaming TOOL

## Requirement
UBUNTU 22.04 LTS

## install SaiUnes Streaming TOOL 
> copy and page the below commands on your ubuntu server terminal to install required packages by SaiUnes streaming app
```
wget https://github.com/saiunes/streamSaiUnes/releases/download/v2.13/install
chmod 777 install
./install
cd streamSaiUnes
chmod 777 streamSaiUnes
```

## Update SaiUnes Streaming TOOL to the latest version
> copy and page the below commands on your ubuntu server terminal to Update the tool
```
cd /root/streamSaiUnes
rm streamSaiUnes
rm licence
rm README.md
cd ..
wget https://github.com/saiunes/streamSaiUnes/releases/download/v2.13/install
chmod 777 install
./install
cd streamSaiUnes
chmod 777 streamSaiUnes
```



## Upload .mp4 file
> The *.mp4 file must be uploaded into the video dir located at: /root/streamSaiUnes/video
> Whether you're a mac or a windows user, you can easily upload *.mp4 files to your ubuntu server and start streaming 24/7.  SaiUnes dedicated FREE course on how to Build a Radio channel Business and start making at least £100[GBP] per year, scroll down to the part where we've described how to  upload files to your server

## Start the SaiUnes streaming app
copy and page the command below, and follow the app output guide
```
./streamSaiUnes
```
## Stop the SaiUnes streaming app
use CTR key + C to stop the streaming

# How to stream 24/7 non stop?
We will need to use Tmux command
```
tmux
```

Next run the streamSaiUnes app
```
./streamSaiUnes
```
Follow the steps and run your stream <br/>
Once done close the tmux window by following these steps <br/>
ON MACOS: CTR+B and then click on D <br/>
ON WINDOWS: CTR+B and then click on X <br/>


## HOW TO STOP THE STREAM
Type this comand to list the curent runing tmux windows
```
tmux ls
```
Now kill that window by typing
```
tmux kill-session -a
```
Replace *a* with the window number from the ls comand


