from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import requests
import re
import os

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
        
        try:
            # 画像ファイルのURLを取得する
            article_img_xpath = "//article/img"
            images = driver.find_elements(By.XPATH, article_img_xpath)

            # 格納先フォルダを生成する
            path = r"imgs\bridge"
            os.makedirs(path, exist_ok=True)

            for index, image in enumerate(images):
                filename = f"image_{index}.png"
                image_path = os.path.join(path, filename)
                image_url = image.get_attribute("src")
                url_patarn = re.compile("^(http|https)://")
                res = url_patarn.match(image_url)

                if res:
                    response = requests.get(image_url, stream=True)

                    with open(image_path, "wb") as f:
                        f.write(response.content)

        except Exception as e:
            print(f"{index}番目の画像ダウンロード・保存時にエラーが発生しました。:{e}")
            print("画像URL:", image_url)

    except Exception as e:
        print(f"アイテムが表示できませんでした。:{e}")

    finally:
        driver.quit()

if __name__ == "__main__":
    main()