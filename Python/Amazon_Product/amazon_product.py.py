from bs4 import BeautifulSoup
import requests
 
# Function for Product name
def product_name(soup):
     
    try:

        # string value of name
        name = soup.find("span", attrs={"id":'productTitle'}).string.strip()
 
    except AttributeError:
        name = ""   
 
    return name
 
# Function for Product Price
def product_price(soup):
 
    try:
        price = soup.find("span", attrs={'id':'priceblock_ourprice'}).string.strip()
 
    except AttributeError:
 
        try:
            # deal price
            price = soup.find("span", attrs={'id':'priceblock_dealprice'}).string.strip()
 
        except:     
            price = ""  
 
    return price
 
# Function for Product Rating
def product_rating(soup):
 
    try:
        rating = soup.find("i", attrs={'class':'a-icon a-icon-star a-star-4-5'}).string.strip()
         
    except AttributeError:
         
        try:
            rating = soup.find("span", attrs={'class':'a-icon-alt'}).string.strip()
        except:
            rating = "" 
 
    return rating
 
  
def scrap_product(Url, Header):
    ## Requesting http
    http = requests.get(Url, headers=Header)
 
    # Creating soup
    soup = BeautifulSoup(http.content, "lxml")
 
    # links as List of Tag Objects
    links = soup.find_all("a", attrs={'class':'a-link-normal s-no-outline'})
 
    
    linkslist = []
 
    # Loop for extracting links from Tag Objects
    i = 5
    for link in links:
        linkslist.append(link.get('href'))
        i -= 1
        if(i==0):
            break
 
 
    # Loop for extracting product details from each link 
    for link in linkslist:
 
        newhttp = requests.get("https://www.amazon.com" + link, headers=Header)
 
        newsoup = BeautifulSoup(newhttp.content, "lxml")
         
        # Display all the informations
        print("Product Name =", product_name(newsoup))
        print("Product Price =", product_price(newsoup))
        print("Product Rating =", product_rating(newsoup))
        print()
        
    
 
if __name__ == '__main__':
 
    # Headers for request
    Header = ({'User-Agent':
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
                'Accept-Language': 'en-US'})
 
    # URL
    Url = input("Enter the Url of the product:\n")
    scrap_product(Url,Header)

    
    