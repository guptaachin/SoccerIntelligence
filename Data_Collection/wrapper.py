import bs4 as bs
import re

def goal_parser(html):

    soup = bs.BeautifulSoup(html, "html5lib")
    raw_content = dict()
    
    try:
        tag =soup.find_all("div", {"class": "tags-bar"})
        raw_content['tag'] = tag[0].a.text
        tag =soup.find_all("div", {"class": "article-header"})
        raw_content['title'] = tag[0].header.h1.text
        tag =soup.find_all("div", {"class": "actions-bar"})
        raw_content['datetime'] = tag[0].time['datetime']
        tag =soup.find_all("div", {"class": "author-details"})
        raw_content['author'] = tag[0].div.div.text
        tag =soup.find_all("div", {"class": "teaser"})
        raw_content['teaser'] = tag[0].text
        tag =soup.find_all("div", {"class": "body"})
        raw_content['body'] = tag[0].text
    except:
        raw_content = None
        print "error"
        
    return raw_content
 
 
def espn_parser(html):
    raw_content = dict()
    try:
        
        soup = bs.BeautifulSoup(html, "html5lib")
        raw_content['title'] = soup.find_all("title")[0].text
        body = ""
        for e in soup.find_all("p"):
            body = body + e.text + " "
        raw_content['body'] = body
        meta = soup.find_all("meta")
        raw_content['issue_date'] =[re.findall('\d+-\d+-\d+T\d+:\d+:\d+Z',str(e)) for e in meta if re.search('\d+-\d+-\d+T\d+:\d+:\d+Z',str(e)) ][0][0]
        
    except:
        raw_content = None
        print "error"
    return raw_content
    
    
def sky_parser(html):
    raw_content = dict()
    try:
        soup =  bs.BeautifulSoup(html, "html5lib")
        raw_content['title'] = soup.find_all("span", {"class": "article__long-title"})[0].text
        body = ""
        body_part = soup.find_all("div", {"class": "article__body"})
        for line in body_part[0].find_all("p"):
            body += line.text
        raw_content['body'] = body
        raw_content['issue_date'] = soup.find_all("p", {"class": "article__header-date-time"})[0].text
    except:
        print "error"
        raw_content = None
    return raw_content