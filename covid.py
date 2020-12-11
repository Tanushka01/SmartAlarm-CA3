import requests


def covid_info() -> str:
    """
    returns a dict of relevant covid information for the current date
    """
    base_url = 'https://api.coronavirus.data.gov.uk/v1/data?'
    filters = 'filters=areaType=nation;areaName=england&structure=' \
              '{"date":"date","areaName":"areaName","newCasesByPublishDate":"newCasesByPublishDate",' \
              '"cumCasesByPublishDate":"cumCasesByPublishDate","newDeathsByDeathDate":"newDeathsByDeathDate",' \
              '"cumDeathsByDeathDate":"cumDeathsByDeathDate"}'
    complete_url = base_url + filters
    covid_stats = requests.get(complete_url).json()
    cases_info = covid_stats['data']
    daily_info = cases_info[0]   # using indexing to extract the latest information
    covid_update = " Covid Update: " + str(daily_info['newCasesByPublishDate']) +\
                   ' new cases reported, bringing the total cases to ' + str(daily_info['cumCasesByPublishDate']) + "."
    return covid_update
