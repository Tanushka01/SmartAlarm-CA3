from time_conversions import*
from news import *
from notifs import displayed_notif
from weather import *
from covid import *
from flask import *
import pyttsx3
import time
import sched
import logging

LOG_FORMAT = '%(levelname)s: %(asctime)s %(message)s'
logging.basicConfig(filename="pysys.log", level=logging.DEBUG, format=LOG_FORMAT)

s = sched.scheduler(time.time, time.sleep)
logging.info("Alarm scheduler set up")
app = Flask(__name__)
speak = pyttsx3.init()
alarms = []


@app.route('/')
@app.route('/index')
def controller():
    """
    This function controls the smart alarm.
    It sets alarms and makes scheduled announcements, and displays relevant information as silent notifications
    """
    s.run(blocking=False)
    notifications = []
    alarm_time = request.args.get("alarm")
    alarm_label = request.args.get("two")
    alarm_item = request.args.get("alarm_item")
    notif_item = request.args.get("notif")
    weather_update = request.args.get("weather")
    news_update = request.args.get("news")
    logging.info("Arguments from webapp extracted")
    notifications = displayed_notif(notifications)  # A list of dicts containing notif info is assigned to notifications
    logging.info("notification list created")

    if alarm_time:
        logging.info("inputted alarm converted to carry out calculations")
        alarm_hhmm = alarm_time[-5:-3] + ':' + alarm_time[-2:]    # formats the alarm time
        new_alarm = {"title": "Alarm set for " + alarm_hhmm, "content": alarm_label}
        alarms.append(new_alarm)      # adds new alarm to the list of alarms
        delay = hhmm_to_seconds(alarm_hhmm) - hhmm_to_seconds(time_now())   # changes alarm time to a delay in seconds
        s.enter(delay, 1, remove_alarm, (new_alarm,))
        logging.info("Alarm time has elapsed")

        if weather_update and news_update:
            logging.info("alarm set for weather and news update")
            # gives a news, weather and covid announcement when alarm goes
            logging.info("Announcement information extracted from API")
            s.enter(delay, 1, announce, (alarm_label + " " + covid_info() + weather_announcement +
                                         " Today's Top Stories are:" + news_ann(),))

        elif weather_update:
            logging.info("alarm set for weather update only")
            # gives weather update along with covid info when alarm goes
            logging.info("relevant announcement information extracted from API")
            s.enter(delay, 1, announce, (alarm_label + " " + covid_info() + weather_announcement,))

        elif news_update:
            logging.info("alarm set for news update only")
            # gives news updates along with covid info when alarm goes
            logging.info("relevant announcement information extracted from API")
            s.enter(delay, 1, announce, (alarm_label + " " + covid_info() + " Today's Top Stories are:" + news_ann(),))

        else:
            logging.info("Standard alarm")
            # announces alarm label followed by a covid update with alarm goes
            logging.info("relevant announcement information extracted from API")
            s.enter(delay, 1, announce, (alarm_label + covid_info(),))
        print("announced at " + alarm_hhmm, "list of alarms:", alarms)
        logging.info("announcement has been made")

    if notif_item:
        # manually remove a notification
        logging.info("user wants to remove notification")
        for i in notifications:
            if i['title'] == notif_item['title']:
                notifications.remove(i)
                logging.info("notif manually removed")

    if alarm_item:
        # cancel an alarm
        logging.info("user wants to cancel alarm")
        for alarm in alarms:
            if alarm_item['title'] == alarm['title']:
                alarms.remove(alarm)
                logging.info("Alarm canceled")

    return render_template('template.html', title='SMART ALARM', notifications=notifications, image='Alarm.png',
                           alarms=alarms)


def remove_alarm(v):
    """
    removes an alarm from the list of alarms
    """
    alarms.remove(v)
    print("announced alarm removed")


@app.route('/announce')
def announce(announcement):
    """
    Converts the argument which is a text, to speech using the pyttsx3 module
    """
    try:
        speak.endLoop()
    except:
        pass
    speak.say(announcement)
    speak.runAndWait()


if __name__ == '__main__':
    app.run()
