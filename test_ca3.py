"""
Testing of the different modules need for the smart alarm
"""
from news import *
from covid import covid_info
from weather import *


def test_covid_info():
    assert (isinstance(covid_info(), str)) == True


def test_weather_info():
    assert (isinstance(weather_info(), tuple)) == True


def test_news_info():
    assert (isinstance(news_info(), tuple)) == True
    assert (isinstance(news_ann(), str)) == True
    assert (isinstance(top_news_story(), list)) == True


def all_tests():
    test_covid_info()
    test_news_info()
    test_weather_info()


all_tests()
