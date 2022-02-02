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
