# Server Side Picture Frame Web App

Welcome to the Server Side Picture Frame Web App, a customized version derived from rcdemuth/pictureframe, itself based on satssehgal/pictureframe.

## Quick Start

1. Download the files.
2. Run `docker-compose up -d`.
3. Access the app on your device at port 5000.
4. Consider setting a static IP for your host machine.

## Docker Compose Configuration

```yaml
version: '3.3'
services:
   picframe:
     image: P8ntBal1551/pictureframe:latest
     ports:
      - "5000:5000"
     volumes:
       - *Your image directory*:/app/config/images
       - /docker/pictureframe:/app/config
     restart: always
     environment:
       - REFRESH_INTERVAL=30
```

## Changes Made

This version of the project was crafted with the help of ChatGPT. The following changes were implemented:

1. **Image Resizing**: Images are now automatically resized to fit the screen size, ensuring optimal display.

2. **Blurred Background**: Added a blurred copy of the image as the background to fill in white space and enhance visual aesthetics.

3. **JavaScript Image Reload**: Replaced the periodic refresh with JavaScript to dynamically fetch and load new images without disrupting the user experience.

4. **Image Folder Relocation**: The image folder was relocated for better organization and ease of use.

5. **Refresh Timer Environment Variable**: Introduced a refresh timer environment variable for flexibility. You can now easily adjust the refresh interval without modifying the code (default: 15 seconds).

6. **Random Image Access**: A new feature allows you to access a random image from your collection by visiting *ipAddress*:5000/getRandomImage.

## Future Changes

- **Update Python Version**: Consider changing the Python version to a more recent release, ensuring compatibility with the latest libraries and features.

## Important Note

This version might have undiscovered bugs; hence, it's recommended to run it locally and avoid exposing it to the internet.

**Attribution**: ChatGPT contributed to the coding and the creation of this README. The collaboration enhanced the project's functionality and documentation.