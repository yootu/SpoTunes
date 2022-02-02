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

