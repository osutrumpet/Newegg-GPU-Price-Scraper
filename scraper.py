from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import time

newegg_url = 'https://www.newegg.com/p/pl?d=graphics+card&page='
list_gpus = [2060,2070,2080,3060,3070,3080]
list_price = []
list_1050 = []



def price_scrape(gpu):
    
    #gather webpage "Graphics card page only
    for x in range(10):
        try:
            uClient = uReq(newegg_url + str(x))
            page_html = uClient.read()
            uClient.close()

            #parse the html from the page using BS4
            page_soup = soup(page_html, "html.parser")
            #find all product
            containers = page_soup.findAll("div",{"class":"item-container"})

            for container in containers:
                title =  container.img["alt"]
                if str(gpu) in title:
                    price_container = container.findAll("li",{"class":"price-current"})
                    price = price_container[0].strong.text
                    list_price.append(price.replace(",",""))
        except AttributeError:
            print("NoneType error thrown during search for: " + str(gpu))
    sumandprint(list_price,gpu)
    list_price.clear()




def sumandprint(li_x,gpu):
    avg = 0
    low = 0
    high = 0
    for x in li_x:
        avg += int(x)
        if low==0:
            low = int(x)
        if  int(x) < low:
            low = int(x)
        if int(x) > high:
            high = int(x)

    if len(li_x) > 0:
        avg = int(avg/len(li_x))
        f.write(str(gpu) + "\n")
        f.write(str(avg) + "\n" + str(low) + "\n" + str(high) + "\n" )





#Enter loop to load data from site every 120
while True:    
    filename = "current.txt"
    f = open(filename, "w")


    start = time.process_time()
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S",t)
    print("Scraping comminessed at " + current_time)
    f.write(str(len(list_gpus))+ "\n")
    for gpus in list_gpus:
        price_scrape(gpus)
    print("Time lapse: "+ str(time.process_time()- start))
    f.close()
    print("Sleeping for 120")
    time.sleep(120)

    