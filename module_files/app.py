import datetime as dt
import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

# set up for sqlalchemy to use sqlite
engine = create_engine("sqlite:///hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)

# set the table classes
Measurement = Base.classes.measurement
Station = Base.classes.station

# session
session = Session(engine)

# define the flask app
app = Flask(__name__)


# html to format the welcome page
html = '''
<html>
    <head>
        <title>
        Flask App
        </title>    
    </head>
    <body>
        <h1>
        Hawaii Climate Analysis API
        </h1>
        <div>
        Available Routes
        </div>
        <div>
            <div>
                <a href="http://127.0.0.1:5000/api/v1.0/precipitation">
                /api/v1.0/precipitation
                </a>
            </div>
            <div>
                <a href="http://127.0.0.1:5000/api/v1.0/stations">
                /api/v1.0/stations
                </a>
            </div>
            <div>
                <a href="http://127.0.0.1:5000/api/v1.0/tobs">
                /api/v1.0/tobs
                </a>
            </div>
            <div>
                <a href="http://127.0.0.1:5000/api/v1.0/temp">
                /api/v1.0/temp/<start>/<end>
                </a>
            </div>
        </div>
    </body>
</html>
'''

@app.route('/')
def welcome():
    return html

@app.route('/api/v1.0/precipitation')
def precipitation():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precipitation = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= prev_year).all()
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)

@app.route('/api/v1.0/stations')
def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)

@app.route('/api/v1.0/tobs')
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).filter(Measurement.station == 'USC00519281').filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)
    
@app.route('/api/v1.0/temp/<start>')
@app.route('/api/v1.0/temp/<start>/<end>')
def stats(start=None, end=None):
    sel = [func.max(Measurement.tobs), func.min(Measurement.tobs), func.avg(Measurement.tobs)]
    
    if not end:
        results = session.query(*sel).filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps=temps)
    
    results = session.query(*sel).filter(Measurement.date >= start).filter(Measure.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)
    