from bs4 import BeautifulSoup
from newspaper import Article
from gtts import gTTS


def txtspeech(weburl):
  article = Article(weburl)

  article.download()
  article.parse()

  txtart = article.text
  tts = gTTS(text=txtart, lang='en')
  tts.save("article.mp3")
  print ("MP3 Saved")



print ("Ganesha")

# http = urllib3.PoolManager()

# weburl = 'https://techcrunch.com/2017/01/09/tesla-moves-towards-greater-autonomy-with-autopilot-rollout-for-hw2-cars/'
# response = http.request('GET', weburl)
# soup = BeautifulSoup(response.data)

# paragraphs = soup.find('headline')

# print (paragraphs)


# content = urllib3.urlopen(weburl).read()
# soup = BeautifulSoup(content)
# print(soup.get_text())




