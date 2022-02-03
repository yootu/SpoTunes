#!/usr/bin/env python

import lib_getify
import lib_track
import concurrent.futures
import rich

#// Use "Better Comments" extension by Aaron Bond for clearer code

def main():
  
  playlist_link = input("Enter playlist link: ")
  
  playlist = lib_getify.getify(playlist_link)
  playlist.get_tracks()

if __name__ == '__main__':
  main()
