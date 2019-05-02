from app import bp, app
from flask import request
from colour import Color
import json
# import time


@app.route('/twinkleset')
def twinkleset():
    bp.desc.animation['typename'] = '$bpa.strip.Twinkle'
    bp.desc.animation['colors'] = '[255, 127, 127], [0, 255, 0]'
    print(bp)
    return "Set Successfully!"


@app.route('/colors/set', methods=["POST"])
def colorssetrgb():
    colorList = request.form.get('colors').split(',')

    colorsString = ""
    for colorName in colorList:
        c = Color(colorName)
        colorsString += "[{},{},{}],".format(
            int(255*c.red), int(255*c.green), int(255*c.blue)
        )
    colorsString = colorsString[0:-1]
    print(colorsString)

    colors = colorsString
    bp.newAnim(
        '$bpa.strip.Twinkle',
        colors
    )
    return "Animation animation set to RGB!"


@app.route('/start')
def startanim():
    bp.start()
    return "Animation started!"


@app.route('/stop')
def stopanim():
    bp.stop()
    return "Animation stopped!"
