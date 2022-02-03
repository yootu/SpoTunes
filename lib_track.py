#!/usr/bin/env python

#? make changes to a local track's properties

from os import system


class Track:
  def __init__(self, index):
    self.index = index
    self.title = str()
    self.album = str()
    self.artist = str()
    self.yt_hash = str()

  #! pass generated youtube link to youtube-dl
  def save_track(self):
    to_save = f"https://www.youtube.com/watch?v={self.yt_hash}"
    print(f"Downloading {self.index}. {self.title} by {self.artist} from the album: {self.album}")
    os.system(f"youtube-dl -f bestaudio {to_save}")

