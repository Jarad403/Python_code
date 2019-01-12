import requests
import time
from bs4 import BeautifulSoup
import re
def download_file():
    sign=1
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36"}
    for number in range(1,162):
        main_url="https://www.html5tricks.com/page/"+str(number)
        response=requests.get(main_url,headers=headers).text
        soup=BeautifulSoup(response,"html.parser")
        id_content=soup.find(id="content")
        articles=id_content.find_all('article')
        for article in articles:
            #获取目标名字
            head=article.find('h1')
            title=head.a.string
            #获取下载地址
            body=article.find(attrs={'class':'download'})
            download_url=body['href']
            #获取下载内容
            result=requests.get(download_url,headers=headers).content
            try:
                with open("E:\\Keep\\"+title+".rar",'wb')as f:
                    f.write(result)
                print("第"+str(sign)+"份文件"+title+".rar----------下载成功！")
            except BaseException:
                print("第"+str(sign)+"份文件"+title+".rar----------下载失败！")
            #反反爬虫睡眠
            time.sleep(3)
            sign=sign+1
if __name__ == '__main__':
    download_file()
