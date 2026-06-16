from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

def main():
    target_url = "https://thebridge.jp/"

    # ヘッドレスモードに設定
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    
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

    display_count = 100

    try:
        if display_count > 12:
            scroll_count = int(display_count/12)+1
        else:
            scroll_count = 1

        for i in range(scroll_count):
            # スクロールするjavascriptを実行する           
            # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # 画面上でEndキーを押下する
            driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
            sleep(3)

        h3_a_xpath = "//h3/a"
        for elem in driver.find_elements(By.XPATH, h3_a_xpath):
            print(elem.text)
            print(elem.get_attribute("href"))

    except Exception as e:
        print(f"アイテムが表示できませんでした。{e}")

    finally:
        driver.quit()

if __name__ == "__main__":
    main()