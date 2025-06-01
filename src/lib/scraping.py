import os

import requests
from bs4 import BeautifulSoup

class Scraping:
    """ウェブサイトから情報を自動的に収集し、必要なデータを抽出・整形する
    
    Args:
        url(str): スクレイピング対象のウェブサイトのURL
    """
    def __init__(self, url:str) -> None:
        self.url = url
    
    def get_html_in_text_format(self) -> str:
        """テキスト形式でHTMLを取得する

        Returns:
            (str): テキスト形式のHTML文字列
        """
        try:
            response = requests.get(self.url)
            # HTTPステータスコードが200番台（成功）でない場合、HTTPError
            response.raise_for_status()
            return response.text
        
        except requests.exceptions.RequestException as e:
            print(f"URLの取得中にエラーが発生しました: {e}")
            return e.__class__.__name__
        
    def convert_to_tree_structure(self, html_in_text_format:str) -> BeautifulSoup:
        """ツリー構造に変換する

        Args:
            html_in_text_format(str):テキスト形式のHTML文字列

        Returns:
            ツリー構造化されたオブジェクト(BeautifulSoup): 
        """
        return BeautifulSoup(html_in_text_format, 'html.parser')
    
    def get_pdf_links_tag(self, soup:BeautifulSoup) -> list[str]:
        """aタグを検索しPDFのリンク一覧を返す

        Args:
            soup(BeautifulSoup):ツリー構造化されたオブジェクト

        Returns:
            pdf_links(list): PDFファイルのリンク一覧
        """

        pdf_links = []
        for link in soup.find_all('a', href=True):
            href = link['href']

            # リンクの最後がpdfの拡張子がある場合
            if href.endswith('.pdf') :
                # 相対URLを絶対URLに変換
                if not href.startswith(('http://', 'https://')):
                    href = requests.compat.urljoin(self.url, href)
                pdf_links.append(href)
        return pdf_links
    
    def is_exist_pdf_links(self, pdf_links:list) -> bool:
        """PDFファイルのリンク一覧の存在確認

        Args:
            pdf_links(list):PDFファイルのリンク一覧

        Returns:
            (bool): True あり false なし
        """
        if len(pdf_links) == 0:
            return False
        return True
    
    def download_pdf_files(self, pdf_links:list, output_folder='downloaded_pdfs') -> None:
        # ダウンロードフォルダを作成
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        for i, pdf_url in enumerate(pdf_links):

            # ファイル名をURLから取得
            file_name = os.path.join(output_folder, os.path.basename(pdf_url))

            try:
                pdf_response = requests.get(pdf_url, stream=True)
                pdf_response.raise_for_status()

                with open(file_name, 'wb') as f:
                    for chunk in pdf_response.iter_content(chunk_size=8192):
                        f.write(chunk)
                print(f"ダウンロード完了: {file_name}")
            except requests.exceptions.RequestException as e:
                print(f"PDFのダウンロード中にエラーが発生しました: {e}")