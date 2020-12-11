from covid import covid_info
from weather import *
from news import *


def displayed_notif(notif_list: list) -> list:
    notif_list.append({'title': 'Total Covid cases ',
                       'content': str(covid_info() + ' Wash your hands, wear a mask and stay safe.')})
    notif_list.append({'title': 'Top News Story', 'content': top_news_story()[0] + " " + top_news_story()[1]})
    notif_list.append({'title': 'The Weather report:',
                       'content':
                           skies + " skies. Temperature ranging from " + b + '-' + a
                           + " degrees. It's cold! Wear a coat"})
    return notif_list
