from flask import Flask
from datetime import datetime, timedelta
app = Flask(__name__)

snoozeUntil = datetime.now()
print("snooze until: " + str(snoozeUntil))

@app.route('/isSnoozed')
def is_snoozed():
    global snoozeUntil
    isSnoozed = snoozeUntil > datetime.now()
    return (str(isSnoozed))

@app.route('/setSnoozeMinutes/<int:addMinutes>')
def add_minutes(addMinutes):
    global snoozeUntil
    snoozeUntil = datetime.now() + timedelta(minutes=addMinutes)
    return ('snooze until: ' + str(snoozeUntil))

@app.route('/resetSnooze')
def reset_snooze():
    global snoozeUntil
    snoozeUntil = datetime.now()
    return ('snooze reset')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
