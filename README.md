# Newegg-GPU-Price-Scrapper
Simple python script that scrapes from Newegg GPU prices using BeautifulSoup the returns Average price highest and lowest price for each series GPU

Currently it outputs the data to a current.txt file which will later be used in tangent with a reddit bot. 
Additionally a sleep function will be added so that the prices update every couple hours. This version runs through 50 of the pages for testing and will out put if it runs into a NoneType error. 

The current.txt file is arranged as so    GPU,Highest price, lowest price, Average Price\n
