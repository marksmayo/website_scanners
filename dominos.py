import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_html(url):
    request_headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }    
    response = requests.get(url, headers=request_headers)
    response.raise_for_status()
    return response.text

def extract_links(soup, selector):
    return [link.get('href') for link in soup.select(selector)]

base_url = 'https://www.dominos.co.nz'

main_page_html = get_html(base_url + '/stores/south-island')

soup_main = BeautifulSoup(main_page_html, 'html.parser')

area_links = extract_links(soup_main, 'div.store-information a[href]')
area_links = list(dict.fromkeys(area_links))
area_links.sort()
print("Area links for " + str(len(area_links)) + " stores :" + str(area_links)) 
print("|Store|Deal|Price from*|Method|Code|\n|-|")    

for area_link in area_links:
    suburbprinted=False
    split_string = area_link.split('/')
    extracted_text = '/'.join(split_string[2:])
    storeurl = (base_url + "/coupon-voucher/" + extracted_text)
    area_html = get_html(storeurl)

    store = BeautifulSoup(area_html, 'html.parser')

    storename = store.select('span.store-name')
    if len(storename) != 0:
        voucher_titles = store.select('div.offer-ribbon-anz')
        voucher_codes = store.select('div.offer-code-anz')
        voucher_method = store.select('p.service-method-anz')
        if len(voucher_titles) == 0:
            print("|[" + storename[0].text.title() + "](" + storeurl + ")")
        else:
            for t,c,m in zip(voucher_titles, voucher_codes, voucher_method):
                if suburbprinted:
                    print("||" + t.text.strip().split('from')[0].strip() + "|" + t.text.strip().split('from')[1].replace("*", "").split(";",1)[0].strip() + "|" + m.text.strip().replace("Only", "").strip() + "|" + c.text.strip().replace("Offer Code: ", "").strip() + "|")
                else:
                    print("|[" + storename[0].text.title() + "](" + storeurl + ")|" + t.text.strip().split('from')[0].strip() + "|" + t.text.strip().split('from')[1].replace("*", "").split(";",1)[0].strip() + "|" + m.text.strip().replace("Only", "").strip() + "|" + c.text.strip().replace("Offer Code: ", "").strip() + "|")
                    suburbprinted = True
