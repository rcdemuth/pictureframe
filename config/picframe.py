import os
from os import listdir
from flask import Flask, render_template, jsonify
from flask_bootstrap import Bootstrap
import random

app = Flask(__name__, template_folder='/app/config/templates', static_folder='/app/config')
flask_bootstrap = Bootstrap(app)

def getImgs():
    img_list = []
    for file in listdir('/app/config/images/'):
        img_list.append(file)
    return random.choice(img_list)

# Get refresh interval from environment variable or default to 15 seconds
refresh_interval = int(os.getenv('REFRESH_INTERVAL', 15))

@app.route('/')
def sendImgs():
    return render_template('index.html', imgs=getImgs(), refresh_interval=refresh_interval)

@app.route('/getRandomImage')
def getRandomImage():
    random_img_path = 'config/images/' + getImgs()
    return jsonify({'imagePath': random_img_path})

if __name__ == '__main__':
    app.run(debug=True)