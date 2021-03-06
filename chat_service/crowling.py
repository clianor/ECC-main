import requests
from bs4 import BeautifulSoup
from . import coordinate

def crowlier_lunch(context):
    req = requests.get('http://www.diningcode.com/list.php?query='+ str(context))

    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    list_name = soup.select(".dc-restaurant-name")
    list_info = soup.select(".dc-restaurant-category")
    list_address = soup.select("dc-restaurant-info")
    lists_name = []
    for list1 in list_name:
        lists_name.append(list1.text.strip('\n'))
    address = []
    for addr in list_address:
        address.append(addr.select('.dc-restaurant-info')[1])
    
    lists_address = []
    for addr in address:
        data = addr.select('.dc-restaurant-info-text')[0].text
        lists_address.append("http://map.daum.net/?q="+coordinate.get_address(data))
   
    lists_info = []
    for list1 in list_info:
        lists_info.append(list1.text)
    lists_name_info = []

    for i in range(0, len(lists_info)):        
        lists_name_info.append(lists_name[i]+"("+lists_info[i]+")")
    return lists_name_info, lists_address

def lunch_category():
    req = requests.get('http://www.diningcode.com/isearch.php?')

    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    list_category = soup.select(".dc-search-food-category-list-item")
    lists_category = []
    for i in range(0, len(list_category)):
        lists_category.append(list_category[i].text)
    
    return lists_category

if __name__ == "__main__":
    crowlier_lunch(context)
    crowlier_category()