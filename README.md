# Newegg-GPU-Price-Scraper and Reddit bot
Simple python script that scrapes from Newegg GPU prices using BeautifulSoup the returns Average price highest and lowest price for each series GPU

Currently it outputs the data to a current.txt file which will later be used in tangent with a reddit bot. 
Additionally a sleep function will be added so that the prices update every couple hours. This version runs through a set number of pages of the pages for testing and will out put if it runs into a NoneType error. 

The current.txt file is arranged as so     number of gpus\n GPU\n Lowest price\n Highest price\n Average Price\n  in order to provide super simple reading for the associated Buddy bot in development


The reddit bot which is run seperatly but utilizes the prices from the current.txt file will respond to !gpu in set subreddit with the current prices for each series in the gpu list. 

NOTE!!!!! The redit bot will not work unless you impliment a config file with you reddit bot login information. For security reasons I did not include this file!
