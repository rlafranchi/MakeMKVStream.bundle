# Plex Media Server Plugin for MakeMKV Streams

This plugin is created for the purpose of supporting BD/DVD playback through Plex Media Server.  [MakeMKV](http://www.makemkv.com) supports streaming Blu-Ray and DVD discs.  The main use case is for Blu-Ray drives that don't support playback.  Typically you would rip the disc and play the media file, but that is time consuming and space consuming.

### Getting Started

To get started, clone this repo into your [plugin directory](https://support.plex.tv/hc/en-us/articles/201106098-How-do-I-find-the-Plug-Ins-folder-) for Plex Media Server.

Pop in a disc into your drive and startup makemkv.  Open up the disc and select the streaming icon.  Once the server is started then you are ready to go.  This plugin fetches info from the web server that is started and by default uses http://localhost:51000, but can be configured to use another server through the gear icon on the channels page in Plex Media Server.

This plugin has only been tested through the web app on MAC OS X.
