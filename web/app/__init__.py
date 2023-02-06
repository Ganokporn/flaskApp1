from flask import Flask
 
app = Flask(__name__, static_folder='static')
 
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = '7e84a023e7357c07b10d8c32fd6e7e33deaee645c3234b8c'
app.config['JSON_AS_ASCII'] = False
 
from app import views  # noqa