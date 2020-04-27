# Football Betting API

*A program designed to predict and bet on football (soccer) matches using halftime results*

This is a program designed to predict football match results and recommend bets to be placed on the "winning" team. The program is trained using `interpret_data.py` and halftime results from old Premier League matches.

Upon running `betting_app` the program will open Google Chrome and assume control of the browser. It will then navigate the web to find live matches and if live matches with sufficient stats are found it will recommend which team to bet on. The program will also output a link to the match in question to make finding it easier.

## Prerequisites

This program has been programed on python 3 and requires the **pandas module**, **beautifulsoup** and **selenium modules** aswell as **wxpython** to run. If you do not have all of them installed already, you can install them using the pip commands:
```
pip3 install pandas
pip3 install bs4
pip3 install selenium
pip3 install wxpython
```

## How to run

This program also uses the **chromedriver extension** for scraping match data from *flashscore.com*. This extension can be downloaded from [Chromedriver](https://chromedriver.chromium.org/downloads).

In order to use chromedriver the program needs to be able to find and acces the webdriver. If you are on a windows based system we would recommend having the executable in the location `C:/webdrivers/chromedriver.exe`.

If your system is not windows based, or if you place the webdriver in another folder, you will need to edit two lines of code in `betting_app.py` to reflect the location of your webdriver:

```
service = Service(r'C:/webdrivers/chromedriver.exe')
driver = webdriver.Chrome(options=options, executable_path=r'C:/webdrivers/chromedriver.exe')
```
Chromedriver is an webdriver that relies on Google Chrome and will not work with other browsers such as firefox or internet explorer


## Disclaimer

Please remember that all betting in any forms involves risk. Be aware and accept this risk before using this program for any kind of betting. Never bet with money you cannot afford to lose. No "safe" betting system has ever been devised and no one can guarantee profits or freedom from loss. No representation is being made that any user will achieve profits or losses similar to those discussed in commits or any other description.
