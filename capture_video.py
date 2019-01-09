import requests
import time
from bs4 import BeautifulSoup
import re

def download_image():
    i=1
    for n in range(1,184):
        key_url = "http://wallpaper.upupoo.com"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36"}
        main_text = requests.get("http://wallpaper.upupoo.com/store/browVi/1-2-0-"+str(i)+".htm", headers=headers).text
        soup = BeautifulSoup(main_text, "html.parser")
        total = soup.find(attrs={"class": "fullDL"})
        dds = total.find_all('dd')
        for dd in dds:
            a_url = dd.find('a')['href']
            url = key_url + a_url
            end_page_text = requests.get(url, headers=headers).text
            pat = re.compile("http://source.upupoo.com/(.*?).mp4")
            video_url = re.search(pat, end_page_text).group(0)
            video = requests.get(video_url, headers=headers).content
            with open("E:\\YourGame\\视频\\background\\" + str(i) + ".mp4", 'wb')as f:
                f.write(video)
            #抓完一个视频休息三秒    
            time.sleep(3)
            print('第' + str(i)+"个视频下载成功！")
            i += 1
            
if __name__ == '__main__':
    download_image()
    
