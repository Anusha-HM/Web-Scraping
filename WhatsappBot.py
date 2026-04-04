import time
from selenium import webdriver
from selenium.webdriver.common.by import By

if __name__ == '__main__':
    my_options = webdriver.ChromeOptions()
    browser = webdriver.Chrome(options=my_options)
    browser.get('https://web.whatsapp.com')
    time.sleep(20)  # Scan QR code in this window

    name_list = ['Gurugalu']

    for name_user in name_list:
        try:
            user = browser.find_element(By.XPATH, '//span[@title="{}"]'.format(name_user))
            user.click()
        except Exception as e:
            print(f"User {name_user} not found: {e}")
            continue  # Skip to next user if contact not found

        try:
            box_message = browser.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
            box_message.send_keys("Hi Shambhavi Here ... using the whatsapp bot")
            time.sleep(2)
            send_button = browser.find_element(By.XPATH, '//button[@data-tab="11"]')
            send_button.click()
            time.sleep(5)
        except Exception as e:
            print(f"Failed to send message to {name_user}: {e}")

    browser.close()