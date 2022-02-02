#!/usr/bin/env python

#? get details from given spotify link

from bs4 import BeautifulSoup as soup
import urllib.request
import lib_track
import re


class getify:
  def __init__(self, link):
    self.link = link
    self.all_tracks = tuple()


  #! returns tuple of all tracks in the given playlist link
  def get_tracks(self):
    all_tracks = list()
    
    page_data = urllib.request.urlopen(self.link).read()
    page_soup = soup(page_data, 'html.parser')
    all_track_details = page_soup.findAll('div', {'class':'tracklist-col name'})

    track_index = 0

    for single_track in all_track_details:
      track_index += 1
      new_track = lib_track.Track(track_index)
      #
      #TODO get details for track into
      #
      all_tracks.append(new_track)

    self.all_tracks = tuple(all_tracks)


  #! get youtube audio link for given track
  def yt_link(self, index):
    track_yt = f"https://www.youtube.com/results?search_query={remove_spaces(self.all_tracks[index])}+official+audio"
    html = urllib.request.urlopen(track_yt)
    result_links = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    
    self.all_tracks[index].yt_hash = result_links[0]

