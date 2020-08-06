from flask import Flask, render_template
from flask_restful import Api
from resources.truck import Truck
import requests
from db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.secret_key = 'secret'
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html');

@app.route('/api/<string:name>')
def show_truck(name):
    # result = requests.get('http://localhost:5000/trucks/name')
    return render_template('index.html', someVar = name)

api.add_resource(Truck, '/trucks/<string:name>')

if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)
