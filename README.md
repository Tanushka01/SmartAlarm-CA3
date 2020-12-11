# SmartAlarm-CA3
A covid aware, alarm clock that keeps you up to date
## Introduction
This is an alarm app that allows users to schedule when they'd like to recieve the latest, most relevant information on the COVID infection rate, Current weather and Top news headlines from BBC news.
The information can be diliverd to the user via textual notifications that require no user scheduling or alternatively, announcements at a scheduled time
## Prerequisites
- Python 3.8 as this is a python program
- weather and news API keys
## Installation 
For this program, you require the following modules:
- pip install Flask
- pip install requests
-pip install pyttsx3

## Getting Started
### The Alarm:
As mentioned above you will require your own news and weather API keys. These can be found at https://newsapi.org/ and https://openweathermap.org/api for news and weather API keys respectively.
Once You have your own API keys, go to the config.json file to enter your keys. In the config.json file u will also be able to edit the name of the city. This determines where your weather information comes from. The default is weather updates of Exeter.
Run CA3main.py to deploy the smart alarm.
Once running, you will be able to set alarms for the current day on when you'd like to receive verbal notifications about the corona virus cases, top news headlines and the weather depending on the conditions your alarm was set with. Once the alarm time has elapsed, the alarm will be removed from the Alarms column.
### Notifications 
Provide you with current relevant Covid,news and weather information if you wish to not set an alarm.
## Details
Author: Tanushka Shankar

License: MIT licence 
