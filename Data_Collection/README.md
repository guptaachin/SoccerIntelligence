# Data Collection

## Data Collection with Python Scrapy (for soccer news)
How to run the project? We enumerate the steps of running the project here.

1. Python [Scrapy](https://scrapy.org/) has to be installed
2. [Create the project](https://docs.scrapy.org/en/latest/intro/tutorial.html#creating-a-project)
3. NewsSpiders.py and wrapper.py has to be in folder /spiders
4. use this command
> scrapy crawl --nolog (spider name) -o out.json


## Data Collection using the Fantasy API.

*NOTE - Please make sure to get a valid API key [click](https://fantasydata.com/) and paste it in the fantasy_api_calls.py line 12*

How to run the project?
We enumerate the steps of running the project here.

1. Order of running the files - 
    1. python get_round_data_by_roundid.py
    2. python get_player_stats_roundid_teamid.py
    3. python get_player_personal_data_by_team.py

2. All the files mentioned above will populate the data folder.
    


