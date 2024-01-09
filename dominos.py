import requests
from bs4 import BeautifulSoup

def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.text

def extract_links(soup, selector):
    return [link.get('href') for link in soup.select(selector)]

def print_voucher_info(storename, title, price, method, code, storeurl, suburbprinted):
    if suburbprinted:
        print(f"||{title}|{price}|{method}|{code}|")
    else:
        print(f"|[{storename}]({storeurl})|{title}|{price}|{method}|{code}|")

base_url = 'https://www.dominos.co.nz'
main_page_html = get_html(f'{base_url}/stores/south-island')
soup_main = BeautifulSoup(main_page_html, 'html.parser')

area_links = sorted(set(extract_links(soup_main, 'div.store-information a[href]')))
print(f"Area links for {len(area_links)} stores: {area_links}")
print("|Store|Deal|Price from*|Method|Code|\n|-|")

for area_link in area_links:
    suburbprinted = False
    storeurl = f"{base_url}/coupon-voucher/{'/'.join(area_link.split('/')[2:])}"
    store_html = get_html(storeurl)
    store_soup = BeautifulSoup(store_html, 'html.parser')

    storename = store_soup.select_one('span.store-name')
    if storename:
        storename = storename.text.title()
        vouchers = zip(store_soup.select('div.offer-ribbon-anz'),
                       store_soup.select('div.offer-code-anz'),
                       store_soup.select('p.service-method-anz'))

        for voucher_title, voucher_code, voucher_method in vouchers:
            title, price = map(str.strip, voucher_title.text.strip().split('from'))
            price = price.replace("*", "").split(";", 1)[0].strip()
            method = voucher_method.text.strip().replace("Only", "").strip()
            code = voucher_code.text.strip().replace("Offer Code: ", "").strip()
            print_voucher_info(storename, title, price, method, code, storeurl, suburbprinted)
            suburbprinted = True
    else:
        print(f"|[{storename}]({storeurl})|No vouchers available|||")
