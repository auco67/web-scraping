from src.lib.scraping import Scraping

def main():
    target_url = "https://kakaku.com/kaden/fan/ranking_2152/"
    response = Scraping(target_url)
    context = response.get_html_in_text_format()
    soup = response.convert_to_tree_structure(context)
    elems = soup.find_all("div", class_="rkgBox")

    for elem in elems:
        print(elem.find("span", class_="rkgBoxNameItem").string)
        print(elem.find("a", class_="rkgBoxLink")["href"])

if __name__ == "__main__":
    main()

