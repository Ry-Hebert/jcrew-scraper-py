import requests
from bs4 import BeautifulSoup
from typing import List

def pages_sitemap() -> List[str]:
    luz_network_response = requests.get("https://www.jcrew.com/sitemap-wex/sitemap-index.xml")
    directory_soup = BeautifulSoup(luz_network_response.text, "html.parser")
    # print("directory_soup Output:")
    # print(directory_soup, '\n')
    directory_urls = [url.text for url in directory_soup.find_all('loc')]
    # print("directory_urls Output:")
    # print(directory_urls, '\n')

    #Sort out product directories from categories and other
    product_directories = []

    for directory_url in directory_urls:
        if directory_url[:45] == 'https://www.jcrew.com/sitemap-wex/sitemap-pdp':
            product_directories.append(directory_url)
    
    
    product_urls = []
    
    for directory_url in product_directories:
        print(directory_url)
        url_response = requests.get(directory_url)
        soup = BeautifulSoup(url_response.text, "html.parser")
        urls = [url.text for url in soup.find_all('loc')]
        product_urls.extend(urls)
        # print("product_urls: ")
        # print(product_urls, '\n')
    return product_urls

pages_sitemap()