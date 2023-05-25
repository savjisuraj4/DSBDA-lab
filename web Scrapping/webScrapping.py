# Beautiful Soup is a Python package for parsing HTML and XML documents. It creates a parse tree for parsed pages that can be used to extract data from HTML, which is useful for web scraping

import requests
from bs4 import BeautifulSoup


# An HTTP header is a field of an HTTP request or response that passes additional context and metadata about the request or response


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'

}

url = "https://www.flipkart.com/hp-smart-tank-all-one-589-multi-function-wifi-color-inkjet-printer/p/itma1449e7e7cc32?pid=PRNGKZB6NY9YMRJN&lid=LSTPRNGKZB6NY9YMRJNZVXMPX&marketplace=FLIPKART&store=6bo%2Ftia%2Fffn%2Ft64&srno=b_1_1&otracker=hp_omu_Best%2Bof%2BElectronics_3_3.dealCard.OMU_D54DFY00C5JD_3&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_2_L2_view-all%2Chp_omu_PINNED_neo%2Fmerchandising_Best%2Bof%2BElectronics_NA_dealCard_cc_3_NA_view-all_3&fm=neo%2Fmerchandising&iid=en_iFXc3xhNmrXU%2F9SwTABbe113R0hpbjIRJL8Rwa8Y%2BdHRRnAwOKujO0Jwlty2hFWEdbMRI472rZEJM4XoWZWfuQ%3D%3D&ppt=browse&ppn=browse&ssid=kime6iy7s00000001684960536743"


def get_reviews(url):
    review = []
    response = requests.get(url, headers=headers)
    soap = BeautifulSoup(response.content, 'html.parser')
    review_containers = soap.find_all('div', {'class': '_1AtVbE'})

    for containers in review_containers:
        divs = containers.findAll('div', {'class': 't-ZTKy'})
        if (divs):
            for div in divs:
                review.append(div.text)
    return review


reviews = get_reviews(url)
for review in reviews:
    print(review)
    print('------')
