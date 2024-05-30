import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

def get_free_proxies():
    url = "https://free-proxy-list.net/"
    soup = bs(requests.get(url).content, 'html.parser')
    proxies = []
    for row in soup.find("table", attrs={"class": "table-striped"}).find_all("tr")[1:]:
        tds = row.find_all("td")
        try:
            ip = tds[0].text.strip()
            port = tds[1].text.strip()
            proxies.append(str(ip) + ":" + str(port))
        except IndexError:
            continue
    print(f"Retrieved {len(proxies)} proxies")
    return proxies

def search(string):
    return f"https://www.amazon.in/s?k={string}&crid=1GOO07QCIP1ML&sprefix={string}%2Caps%2C216&ref=nb_sb_noss_1"

def page_content(url, proxies):
    for i, proxy in enumerate(proxies):
        print(f"Using proxy {proxy}")
        try:
            response = requests.get(url, proxies={"http": proxy, "https": proxy}, timeout=3)
            if response.status_code == 200:
                print(f"Successfully fetched content with proxy {proxy}")
                return response.content
            else:
                print(f"Failed using proxy {proxy}")
        except Exception as fk:
            print("error use another proxy")
    return None

def total_results(soup):
    try:
        results_tag = soup.find('div', class_='a-section a-spacing-small a-spacing-top-small')
        if results_tag:
            return results_tag.get_text(strip=True)
        return "Total results not found."
    except Exception as fk:
        print(f"Error extracting total results : {fk}")
        return None

def product_info(soup):
    try:
        products = []
        pd_name = soup.find_all('span', class_='a-size-medium a-color-base a-text-normal')
        pd_price = soup.find_all('span', class_='a-price-whole')
        pd_rating = soup.find_all('span', class_='a-icon-alt')

        for name, price, rating in zip(pd_name, pd_price, pd_rating):
            pd_name = name.get_text(strip=True)
            pd_price = price.get_text(strip=True)
            pd_rating = rating.get_text(strip=True)
            products.append([pd_name, pd_price, pd_rating])

        return products
    except Exception as fk:
        print(f"Error extracting product info: {fk}")
        return []

def save_csv(data, filename='products.csv'):
    try:
        df = pd.DataFrame(data, columns=['Name', 'Price', 'Rating'])
        df.to_csv(filename, index=False)
        print(f"Data saved to {filename}")
    except Exception as fk:
        print(f"error saving to CSV: {fk}")

def main():
    item = input("Enter the item to search: ")
    url = search(item)
    proxies = get_free_proxies()
    # print(proxies[0])
    page = page_content(url, proxies)
    # print(page)
    if page:
        soup = bs(page, 'html.parser')
        result = total_results(soup)
        print(result)
        products_info = product_info(soup)
        df = pd.DataFrame(products_info, columns=['Name', 'Price', 'Rating'])
        print(df)
        save_csv(products_info)
    else:
        print("Failed to retrieve page content.")

if __name__ == "__main__":
    main()
