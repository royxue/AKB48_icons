import re
import urllib
import urllib2
from bs4 import BeautifulSoup


def akb_cralwer():
    akb_url = "http://www.akb48.co.jp/about/members/"
    pat = re.compile(r'0511%2F(.*?)_png%2F(.*?).png')

    try:
        html = urllib2.urlopen(akb_url).read()
        soup = BeautifulSoup(html)

        for mmb in soup.find_all('img', width=170):
            img_link = "http:" + mmb.get('src')
            mmb_info = re.findall(pat, img_link)
            img_name = "%s_%s.png" % (mmb_info[0][0], mmb_info[0][1])
            urllib.urlretrieve(img_link, img_name)
            print "%s == Get" % (mmb_info[0][1])

    except Exception as e:
        print e

    finally:
        "Now you get all AKB icons"

if __name__ == "__main__":
    akb_cralwer()
