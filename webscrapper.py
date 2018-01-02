import os

from selenium import webdriver
from bs4 import BeautifulSoup



def getCategoryData():
    driver = webdriver.Chrome("G:\\chromedriver.exe")

    driver.get("http://www.shoppersstop.com")

    html = driver.page_source

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


def writeToFile(category):
    fileDir = os.path.dirname(os.path.realpath('__file__'))
    filename = os.path.join(fileDir, 'impex_placeholder/categories1.impex')

    print type(category)
    with open( 'impex_placeholder/categories1.impex',"w") as f:
        f.write(category)
        f.write("hallelujah")
        f.close()
    
def file_get_contents(filename):
    fileDir = os.path.dirname(os.path.realpath('__file__'))
    filename = os.path.join(fileDir, 'impex_placeholder\categories.impex')
    print filename
    print os.path.exists(filename)
    if os.path.exists(filename):
        fp = open(filename, "r")
        content = fp.read()
        fp.close()
        return content

category_placeholderData = file_get_contents("")
writeToFile(category_placeholderData)

    
    
