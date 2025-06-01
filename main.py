import sys
from src.lib.scraping import Scraping

def run(target_url:str):
    scraping = Scraping(target_url)
    html_in_text_format = scraping.get_html_in_text_format()
    soup = scraping.convert_to_tree_structure(html_in_text_format=html_in_text_format)
    pdf_links = scraping.get_pdf_links_tag(soup=soup)
    if scraping.is_exist_pdf_links(pdf_links=pdf_links):
        scraping.download_pdf_files(pdf_links=pdf_links)

if __name__ == "__main__":
    # target_url = "https://www.pref.saitama.lg.jp/e1701/documents/poster/poster-keji.html"
    # run(target_url=target_url)
    run(sys.argv[1])