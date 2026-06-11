from src.lib.scraping import Scraping

def main():
    target_url = "https://www.yahoo.co.jp/"
    web_page = Scraping(url=target_url)
    context = web_page.get_html_in_text_format()
    soup = web_page.convert_to_tree_structure(context)

    elems = soup.find_all("li", class_="_2j0udhv5jERZtYzddeDwcv")
    pickup_links = [elem.find("a", class_="yMWCYupQNdgppL-NV6sMi")["href"] for elem in elems]

    for pickup_link in pickup_links:
        pickup_web_page = Scraping(pickup_link)
        pickup_context = pickup_web_page.get_html_in_text_format()
        pickup_soup = pickup_web_page.convert_to_tree_structure(pickup_context)
        pickup_elems = pickup_soup.find("div", class_="sc-gdv5m1-8 iubQsz")
        if pickup_elems:
            new_link = pickup_elems.a.attrs["href"]
            print(new_link)

            new_web_page = Scraping(new_link)
            new_context = new_web_page.get_html_in_text_format()
            new_soup = new_web_page.convert_to_tree_structure(new_context)
            print(new_soup.title.text)
            print(new_soup.find(class_="article_body highLightSearchTarget").text, end="\n\n\n")


if __name__ == "__main__":
    main()