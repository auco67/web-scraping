# Webスクレイピング

## 使用方法（Windowsの場合）
1. githubからリポジトリをgit cloneする
    ```
    git clone https://github.com/takahiroanno2024/poster-map.git
    ```
2. main.batを実行する
    
    main.batの中身

    ```
    cd dist
    main.exe https://www.pref.saitama.lg.jp/e1701/documents/poster/poster-keji.html
    ```

    distフォルダ直下にdownloaded_pdfsフォルダが自動生成され、PDFファイルが格納される
    ```
    web-scraping
     ├─dist
     |  ├─downloaded_pdfs
     |  |  ├─01-01-nishi-list-r05chiji.pdf
     |  |  ├─01-02kita-list.pdf
     |  |  ├─・・・
     |  ├─main.exe
     |  ├─・・・
    ```

    ※Webスクレイピングしたサイトは、[埼玉県の第50回衆議院議員総選挙（令和6年10月27日執行）におけるポスター掲示場](https://www.pref.saitama.lg.jp/e1701/documents/poster/poster-keji.html)

## 応用方法
PDFファイルが`a`タグでリンク付けされているサイトであればダウンロードが可能

その場合、main.batの中身を書き換える

main.batの中身
```
cd dist
main.exe ** ここにPDFファイルが<a herf>タグでリンク付けされているサイトのURLを貼り付ける **
```