# Server Side Picture Frame Web App

This is a fork of satssehgal/pictureframe.  I wanted to use a folder on my nas, and that didn't work with the original version, I edited this one to use 2 volumes, one for images and one for the config folder.

This is a very simple server side picture frame web application that you could use to host photos and display them on a computer, phone, or even hang a tablet on a wall and build a rotating image picture frame. 

Simply create a folder called 'img' and place the docker-compose file in the same directory. Move any image you want into the img folder and watch it come to life on all your devices. No more SD cards or external storage needed for each device. See below for the simple docker-compose file

Download the files and run 'docker-compose up -d' and you're set. It will launch on your device at port 5000. Its a good idea to have a static ip for your host machine




