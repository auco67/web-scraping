from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

def main():
    target_url = "https://thebridge.jp/"

    # ヘッドレスモードに設定
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    
    driver = webdriver.Chrome(options=options)
    driver.get(target_url)

    search_word = "フィンテック"

    button_xpath = "//button[contains(@class, 'header-search')]"
    search_button = driver.find_element(By.XPATH, button_xpath)
    search_button.click()

    input_xpath = "//input[@type='search']"
    search_input = driver.find_element(By.XPATH, input_xpath)
    search_input.send_keys(search_word)

    # フォームをSubmitする場合
    # search_input.submit()

    # フォームでEnterキーを押下する場合
    search_input.send_keys(Keys.ENTER)

    sleep(10)

    h3_a_xpath = "//h3/a"
    for elem in driver.find_elements(By.XPATH, h3_a_xpath):
        print(elem.text)
        print(elem.get_attribute("href"))

if __name__ == "__main__":
    main()