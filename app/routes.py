from app import bp, app
from flask import request
from colour import Color
# import json
# import time


@app.route('/colors/set/single', methods=["POST"])
def colorSetSingle():
    """
    Sets the animation to use a single color.
    API expects a `color` name that is valid according to pyColour.
    """
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


@app.route('/colors/set/multi', methods=["POST"])
def colorSetMulti():
    """
    Sets the animation to use a custom list of colors.
    API expects a list of `color` names that are valid according to pyColour.
    """
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


@app.route('/colors/reset', methods=["POST"])
def colorReset():
    """
    Reset the list of colors in the animation back to a pre-defined default.
    """
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


@app.route('/colors/append', methods=["POST"])
def colorAppend():
    """
    Appends a given color or list of colors to the existing animation.
    Color names provided must be valid according to pyColour
    """
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


@app.route('anim/set/custom', methods=['POST'])
def animSetCustom():
    """
    Permanently reset the default animation to a custom definition.
    API should expect json object of a `desc`.
    """
    return "TODO"


@app.route('anim/set/defined', methods=['POST'])
def animSetDefined():
    """
    Permanently reset the default animation to pre-defined value.
    API should expect an animation name to search in the database.
    """
    return "TODO"


@app.route('/anim/temp/custom', methods=["POST"])
def animTempCustom():
    """
    Temporarily play a custom animation for a set amount of time.
    API should expect a full `desc` obect in json alongside a timelimit, in ms.
    """
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


@app.route('/anim/temp/defined', methods=["POST"])
def animTempDefined():
    """
    Temporarily play a pre-defined animation for a set amount of time.
    API should expect an animation name in the database a timelimit,
        in ms.
    """
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
