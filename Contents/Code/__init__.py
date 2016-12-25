###################################################################################################
CHANNEL_NAME = "MakeMKV Stream"
BASE_URL = "http://localhost:51000"

###################################################################################################
def Start():

  ObjectContainer.title1 = CHANNEL_NAME
  HTTP.CacheTime = CACHE_1DAY
  HTTP.Headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/601.2.7 (KHTML, like Gecko) Version/9.0.1 Safari/601.2.7'

####################################################################################################
@handler('/video/makemkvstream', CHANNEL_NAME)
def VideoMainMenu():

  Log('Hey')
  oc = ObjectContainer()
  oc.add(VideoClipObject(
    url = 'http://127.0.0.1:51000/stream/title1.m2ts',
    summary = 'Summary',
    title = 'title',
    thumb = '',
  ))

  return oc
