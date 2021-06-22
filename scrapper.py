from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

newegg_url = 'https://www.newegg.com/p/pl?d=graphics+card'
list_2060 = []
list_1050 = []

filename = "current.txt"
f = open(filename, "w")

def price_scrape():
    #gather webpage "Graphics card page only
    uClient = uReq(newegg_url)
    page_html = uClient.read()
    uClient.close()

    #parse the html from the page using BS4
    page_soup = soup(page_html, "html.parser")
    #find all product
    containers = page_soup.findAll("div",{"class":"item-container"})

    for container in containers:
        title =  container.img["alt"]
        if "2060" in title:
            price_container = container.findAll("li",{"class":"price-current"})
            price = price_container[0].strong.text
            list_2060.append(price)

        if "1050" in title:
            price_container = container.findAll("li",{"class":"price-current"})
            price = price_container[0].strong.text
            list_1050.append(price)


def sumandprint(li_x):
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

    avg = int(avg/len(li_x))
    f.write(str(avg) + "," + str(low) + "," + str(high) + "\n" )
    print("Avg: "+ str(avg))
    print("Low: " + str(low))
    print("High: " + str(high))
    
price_scrape()
f.write("2060,")
sumandprint(list_2060)
f.write("1050")
sumandprint(list_1050)
f.close()
#TODO change this to a for loop that will loop thru the list of different GPU's that will then scrape that gpu then print it.