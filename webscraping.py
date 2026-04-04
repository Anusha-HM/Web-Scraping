from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import csv

class one():
    def __init__(self,title,price):
        self.title = title
        self.price = price

class two():
    def data(self,name):
        count=1
        page=1
        add_page=10
        maximum=100

        my_list=[]

        url="https://www.amazon.com/s?k=" + name +"&page=" + str(page)

        my_options=Options()
        my_options.headless = False
        my_options.add_experimental_option("detach", True)
        my_browser = webdriver.Chrome(ChromeDriverManager().install(),options=my_options)
        my_browser.maximize_window()
        my_browser.get(url)
        my_browser.set_page_load_timeout(12)

        while True:
            try:
                if add_page*page>maximum:
                    break

                if count>add_page:
                    count=1
                    page+=1

                title_path='//*[@id="462b3e4e-5b4c-4064-80ab-db50f049d310"]/div/div/span/div/div/div/div['+str(count)+']/div/div/div[1]/a/h2/span'
                title=my_browser.find_element(By.XPATH, title_path)
                title_text=title.get_attribute('innerHTML').splitlines()[0]
                title.click()

                price_path='//*[@id="priceblock_ourprice"'
                price=my_browser.find_element(By.XPATH, price_path)
                price_text=price.get_attribute('innerHTML')

                url="https://www.amazon.com/s?k==iphone+17+pro+max"
                my_browser.get(url)
                my_browser.set_page_load_timeout(12)

                my_info=one(title_text,price_text)
                my_list.append(my_info)

                count+=1

            except Exception as e:
                print("Exception on the count number",count,e)
                count+=1

                if add_page*page>maximum:
                    break

                if count>add_page:
                    count=1
                    page+=1

                url = "https://www.amazon.com/s?k==iphone+17+pro+max"
                my_browser.get(url)
                my_browser.set_page_load_timeout(12)

        my_browser.close()
        return my_list

fun_call=two()
with open('one.csv', 'w', newline='',encoding='utf-8') as csvfile:
    data=csv.writer(csvfile,delimiter=';',quotechar='"',quoting=csv.QUOTE_MINIMAL)
    for article in fun_call.data("iphone 17 pro max"):
        data.writerow([article.title,article.price])
