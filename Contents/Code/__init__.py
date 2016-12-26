###################################################################################################
CHANNEL_NAME = "MakeMKV Stream"
BASE_URL = "http://127.0.0.1:51000"

###################################################################################################
def Start():

  ObjectContainer.title1 = CHANNEL_NAME
  HTTP.CacheTime = 1
  HTTP.Headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/601.2.7 (KHTML, like Gecko) Version/9.0.1 Safari/601.2.7'

####################################################################################################
@handler('/video/makemkvstream', CHANNEL_NAME)
def VideoMainMenu():
  titles = HTML.ElementFromURL(BASE_URL + '/web/titles', cacheTime=1).xpath('//tr/td[2]') 
  # values = html.xpath('.//table/tbody/tr/td[2]/text()')
  # keys = html.xpath('.//table/tbody/tr/td[1]/text()')
  # Log(html.xpath('.//table/tbody/tr/text()'))
  # Log(html.xpath('//html/body/table')[0].text)
  title = titles[1].text
  count = int(titles[2].text)

  oc = ObjectContainer()

  i = 3
  while i < count + 3:
    oc.add(VideoClipObject(
      url = titles[i].xpath('.//a/@href')[0],
      summary = title,
      title = titles[i].xpath('.//a')[0].text,
      thumb = '',
    ))
    i += 1

  return oc
