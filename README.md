# football_betting_api
**A program designed to predict and bet on football (soccer) matches using halftime results**

***This program requires the pandas module to run, if you do not have it you can install it with an installer such as pip using the command "pip3 install pandas" if on python 3. This program also requires the beautifulsoup and selenium modules to run, these can be downloaded in the same way as the pandas module using the command "pip3 install bs4" and "pip3 install selenium".*** 

**This program also uses the chromedriver extension for scraping match data from flashscore.com. This extension can be downloaded from [Chromedriver](https://chromedriver.chromium.org/downloads). In order to use chromedriver the program needs to be able to find and acces the webdriver. If you are on a windows based system we would recommend creating a folder named "webdrivers" inside your windows C:\ folder and placing the downloaded chromedriver.exe in that folder, the path should then be 'C:/webdrivers/chromedriver.exe'. If your system is not windows based or if you place the webdriver in another folder you will need to edit service = Service(r'C:/webdrivers/chromedriver.exe') in the main betting_app program to reflect the location of your webdriver. Chromedriver is an webdriver that relies on Google Chrome and will not work with other browsers such as firefox or internet explorer**

This is a program designed to predict football match results in halftime and allow bets to be placed on the "winning" team. The program is trained using the interpret_data file and old Premier League matches. Upon running the betting_app file the program will open Google Chrome and assume control of the browser. It will then navigate the web to find live matches and if live matches with sufficient stats are found it will recommend which team to bet on. The program will also output a link to the match in question to make finding it easier.  

Please remember that all betting in any forms involves risk. Be aware and accept this risk before using this program for any kind of betting. Never bet with money you cannot afford to lose. No "safe" betting system has ever been devised and no one can guarantee profits or freedom from loss. No representation is being made that any user will achieve profits or losses similar to those discussed in commits or any other description.


