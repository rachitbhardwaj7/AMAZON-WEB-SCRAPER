from project import get_free_proxies,search,total_results,product_info
from bs4 import BeautifulSoup
import pytest

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36'
}
def main():
    test_search()
    test_get_free_proxies()
    test_product_info()
def test_search():
    assert search("cs50harvard") =="https://www.amazon.in/s?k=cs50harvard&crid=1GOO07QCIP1ML&sprefix=cs50harvard%2Caps%2C216&ref=nb_sb_noss_1"
    assert search("laptop") == "https://www.amazon.in/s?k=laptop&crid=1GOO07QCIP1ML&sprefix=laptop%2Caps%2C216&ref=nb_sb_noss_1"
    assert search("python books") == "https://www.amazon.in/s?k=python books&crid=1GOO07QCIP1ML&sprefix=python books%2Caps%2C216&ref=nb_sb_noss_1"

def test_get_free_proxies():
    proxies = get_free_proxies()
    assert proxies is not None
    assert len(proxies) > 0

def test_product_info():
    test_html = '''
    <div>
        <span class="a-size-medium a-color-base a-text-normal">Product 1</span>
        <span class="a-price-whole">100</span>
        <span class="a-icon-alt">4.5 out of 5 stars</span>
    </div>
    <div>
        <span class="a-size-medium a-color-base a-text-normal">Product 2</span>
        <span class="a-price-whole">50</span>
        <span class="a-icon-alt">3.5 out of 5 stars</span>
    </div>
    '''
    soup = BeautifulSoup(test_html, 'html.parser')
    products_info = product_info(soup)
    assert len(products_info) == 2
    assert products_info[0] == ['Product 1', '100', '4.5 out of 5 stars']
    assert products_info[1] == ['Product 2', '50', '3.5 out of 5 stars']

if __name__ == "__main__":
    main()




# def test_function_3():
