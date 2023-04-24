# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    spider.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: begarijo <begarijo@student.42malaga.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/21 18:18:04 by begarijo          #+#    #+#              #
#    Updated: 2023/04/24 19:58:23 by begarijo         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!usr/bin/env python3

import requests, os, argparse
from bs4 import BeautifulSoup as soup
from urllib.parse import urlparse

found_url = set()
found_img = set()

def arguments():
    arg = argparse.ArgumentParser(description="Web Scrapping")
    arg.add_argument("URL", help="URL to scrape", type=str)
    arg.add_argument("-r", help="Recursive scrapping", action="store_true")
    arg.add_argument("-l", help="Depth level to recursively scrap", type=int, default=5)
    arg.add_argument("-p", help="Path where the info is saved", action="store_true", default="./data/")
    return arg.parse_args()

def find_sites(sites, level):
    try:
        ans = requests.get(sites, timeout=5)
        if (ans.status_code == 200):
            xml = soup(ans.content, "html.parser")
            links = xml.find_all("a")
            for link in links:
                url = link.get("href")
                if url not in found_url:
                    found_url.add(url)
                    if l < level:
                        find_sites(url, l + 1)
    except:
        print("por queeeee")

def find_imgs(sites):
    try:
        ans = requests.get(sites, timeout=1)
        if (ans.status_code == 200):
            xml = soup(ans.content, "html.parser")
            links = xml.find_all("img")
            for link in links:
                url = link.get("src")
                if url not in found_img and valid(url):
                    found_img.add(url)
    except:
        print("juju")

def valid(img):
    exts = ["jpg", "jpeg", "png", "gif", "bmp"]
    for ext in exts:
        if img.endswith(ext):
            return True
        return False

def down_img(imgs, p):
    try:
        for img in imgs:
            ans = requests.get(img, timeout=5)
            if (ans.status_code == 200):
                name = img.split('/')[-1]
                if not os.path.exists(p):
                    print("5")
                    os.makedirs(p)
                with open(p + "/" + name, "wb")  as file:
                    print("cochino")
                    file.write(ans.content)
    except:
        print()


if (__name__=='__main__'):
    args = arguments()
    global url, r, l, p
    url = args.URL
    r = args.r
    l = args.l
    p = args.p

    if r:
        find_sites(url, 0)
    else:
        found_url.add(url)
    print(found_url)
    for url in found_url:
       find_imgs(url)
       down_img(found_img, p)
