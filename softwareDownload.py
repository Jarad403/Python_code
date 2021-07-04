from bs4 import BeautifulSoup
import requests
import time
import os
import re


# 主方法
def main():
    error_list = []
    s = requests.session()
    s.keep_alive = False
    for main_count in range(1, 10):
        t = s.get(MAIN_HOST + "page/" + str(main_count), headers=headers).text
        soup = BeautifulSoup(t, "html.parser")
        div_box = soup.find(attrs={'class': 'article'})
        article_list = div_box.find_all("article")
        for article in article_list:
            try:
                name, real_url = get_real_url(s, article.a['href'])
                print("[info] real_url : " + real_url)
                save_file(name, requests.get(real_url, headers=headers).content)
            except BaseException:
                print("\033[1;35m ERROR!!!\033[0m")
                error_list.append(name)
            time.sleep(3)
        time.sleep(3)
    print("\033[1;31mError : \033[1;37m" + str(error_list))


def get_real_url(session, url):
    print("[info] to " + url)
    t = session.get(url, headers=headers).text
    p_box = BeautifulSoup(t, "html.parser").find(attrs={'class': 'entry-content'}).find_all('p')
    # print(p_box)
    soft_name_in_url_text = p_box[-1].a['href']
    print("[info] software name in url contant : " + soft_name_in_url_text)
    soft_name_in_url = re.search(r'\?(.+)', soft_name_in_url_text).group(1)
    print("[info] get software name in url " + soft_name_in_url + " success...")
    soft_name_text = p_box[-2].span.contents[0]
    print("[info] software name contant : " + soft_name_text)
    soft_name = re.search(r'File(.*):(.+).exe', soft_name_text).group(2).strip()
    print("[info] get software name " + soft_name + " success...")
    # path: /files/download/{soft_name_in_url}/{soft_name}.zip
    return soft_name, MAIN_HOST + "files/download/" + soft_name_in_url + "/" + soft_name + ".zip"


def save_file(name, content):
    save_path = os.path.join(r"E:\A_Box\sordum", name + ".zip")
    with open(save_path, "wb+")as f:
        print("[info] save file to ", save_path + "...")
        f.write(content)
        print("[info] save done...")


if __name__ == '__main__':
    main()
