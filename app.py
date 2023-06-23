from datetime import datetime

import pytz
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Setting up SQLite database configuration for Flask-SQLAlchemy
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///aqms_data.db"
# Creating SQLAlchemy instance
db = SQLAlchemy(app)
# Model for the air quality data
class AirData(db.Model):
    # Definition of the columns in the AirData table
    id = db.Column(db.Integer, primary_key=True)
    dev_eui = db.Column(db.String(16), nullable=True)
    temperature = db.Column(db.Float, nullable=True)
    humidity = db.Column(db.Float, nullable=True)
    voc = db.Column(db.Float, nullable=True)
    o3 = db.Column(db.Float, nullable=True)
    co2 = db.Column(db.Float, nullable=True)
    pm10 = db.Column(db.Float, nullable=True)
    pm4 = db.Column(db.Float, nullable=True)
    pm2_5 = db.Column(db.Float, nullable=True)
    pm1 = db.Column(db.Float, nullable=True)
    flame = db.Column(db.Boolean, nullable=True)
    date_created = db.Column(db.DateTime, default=datetime.utcnow())

    def repr(self):
        return '<Info %r>' % self.id


# Model for the email recipients
class Emails(db.Model):
    # Definition of the columns in the Emails table
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), nullable=False)

    def repr(self):
        return '<Email %r>' % self.id


# With the application context, create all the tables as per the models
with app.app_context():
    db.create_all()

@app.route('/', methods=['POST', 'GET'])
def main():  # put application's code here
    if request.method == 'POST':
        # Parsing the incoming POST request
        baghdad_tz = pytz.timezone('Asia/Baghdad')
        eui = request.json["end_device_ids"]["dev_eui"]
        if 'decoded_payload' in request.json['uplink_message']:
            decoded_payload = request.json['uplink_message']['decoded_payload']
            co2Val = decoded_payload.get("co2", decoded_payload.get("temperature_1"))
            o3Val = decoded_payload.get("o3", decoded_payload.get("analog_in_3"))
            try:
                new_info = AirData(dev_eui=eui,
                                   temperature=request.json["uplink_message"]["decoded_payload"]["temperature_5"],
                                   humidity=request.json["uplink_message"]["decoded_payload"][
                                       "relative_humidity_6"],
                                   o3=o3Val, voc=request.json["uplink_message"]["decoded_payload"]["temperature_4"],
                                   co2=co2Val,
                                   pm1=request.json["uplink_message"]["decoded_payload"]["temperature_7"],
                                   pm2_5=request.json["uplink_message"]["decoded_payload"]["temperature_8"],
                                   pm4=request.json["uplink_message"]["decoded_payload"]["temperature_9"],
                                   pm10=request.json["uplink_message"]["decoded_payload"]["temperature_10"],
                                   flame=request.json["uplink_message"]["decoded_payload"]["digital_in_2"],
                                   date_created=datetime.utcnow().replace(tzinfo=pytz.utc).astimezone(
                                       baghdad_tz))
                # Adding and committing the air quality data to the database
                db.session.add(new_info)
                db.session.commit()
                return redirect('/')

            except Exception as e:
                print(e)
                return "Fail"
        else:
            return redirect('/')
    else:
        return render_template('mainPage.html')

@app.route('/show')
def Display():
    return render_template('showData.html')


if __name__ == '__main__':
    app.run()
