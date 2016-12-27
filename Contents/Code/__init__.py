###################################################################################################
CHANNEL_NAME = "MakeMKV Stream"
BASE_URL = "http://%s:%s" % (Prefs['host'], Prefs['port'])

###################################################################################################
def Start():

  ObjectContainer.title1 = CHANNEL_NAME
  HTTP.CacheTime = 1
  HTTP.Headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/601.2.7 (KHTML, like Gecko) Version/9.0.1 Safari/601.2.7'

####################################################################################################
@handler('/video/makemkvstream', CHANNEL_NAME)
def VideoMainMenu():
  titles = HTML.ElementFromURL(BASE_URL + '/web/titles').xpath('//tr/td[2]') 
  keys = HTML.ElementFromURL(BASE_URL + '/web/titles').xpath('//tr/td[1]') 
  title = titles[1].text

  
  count_index = 1
  count_str = keys[count_index].text
  while count_str != 'titlecount':
    count_index += 1
    count_str = keys[count_index].text

  count = int(titles[count_index].text)
  count_index += 1

  oc = ObjectContainer()

  i = 0
  while i < count:
    oc.add(VideoClipObject(
      url = titles[count_index].xpath('.//a/@href')[0],
      summary = title,
      title = keys[count_index].text,
      thumb = '',
    ))
    count_index += 1
    i += 1

  return oc
