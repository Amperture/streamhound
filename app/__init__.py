from flask import Flask
from app.AnimationController import AnimationController

app = Flask(__name__)
bp = AnimationController()

from app import routes
