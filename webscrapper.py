from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome("G:\\chromedriver.exe")

driver.get("http://www.shoppersstop.com")

html = driver.page_source

def p(x):
    print x
    
soup = BeautifulSoup(html, 'html.parser');
D={}
category={}  
for child in soup.select('.nav-wrap > ul > li.fn-l1-categories-list-item'):
 
     
    supercategory= child.find('a')
    if supercategory is not None:
        subsubcategory = list()
        for subchild in child.select('.sub-main-menu > ul > li > div > ul > li > div'):
            
            subchildDict={}
            subcategory = subchild.select('span > a')
            for subsubsubmenu in subchild.select('ul > li > a'):
                subsubcategory.append(subsubsubmenu.get_text())
            subchildDict[subchild.get_text()]= subsubcategory
        category[supercategory.get_text()]=subsubcategory
for i in category:
    print i, category[i]
