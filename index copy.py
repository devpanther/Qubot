
def crawl():
    # crawl a website and click on a link

    # import libraries
    import requests as req  # for requesting websites
    from bs4 import BeautifulSoup as bs  # for parsing html

    # get the website
    agent = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
    session = req.Session()

    payload = {
        'channelid': 'https://www.youtube.com/channel/UCKQvGU-qtjEthINeViNbn6A',
    }

    s = session.post(
        "https://mytoolstown.com/youtube/check_account.php", data=payload,  headers=agent)


    # Navigate to the next page and scrape the data
    s = session.get('https://mytoolstown.com/youtube/earn/');

    t = session.get(
        'https://mytoolstown.com/youtube/earn/getData.php?kNeT=JKLCM%18HI%19%1A%1FINB%1E%18IMI%1A&type=A')

    soup = bs(s.text, 'html.parser')

    text = soup.find('h5', {'class': 'card-title'}).text
    name = t.json()['fromuser']
    link = t.json()['link']
    type = t.json()['type']
    id = t.json()['promotionid']

    # add href to the button
    soup.find('a', {'id': 'actionbtn'})['onclick'] = "startwindow('4361759','https://www.youtube.com/channel/UCrG7vaUWXTGrPn0Shdd6n6g?__a=1','Subscribe',2)"

    print(soup.find('a', {'id': 'actionbtn'})['onclick'])

    print(text) # print the text
    print(name) # print the name
    print(link) # print the link
    print(type) # print the type
    print(id) # print the id


if 1 == 1:
    crawl() # run the function