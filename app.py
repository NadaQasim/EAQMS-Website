from datetime import datetime
from flask import Flask, render_template
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
    nox = db.Column(db.Float, nullable=True)
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


@app.route('/')
def Display():  # put application's code here
    return render_template('showData.html')


if __name__ == '__main__':
    app.run()
