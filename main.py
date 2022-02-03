#!/usr/bin/env python

import lib_getify
import lib_track
import concurrent.futures
import rich

#// Use "Better Comments" extension by Aaron Bond for clearer code

def main():
  print(" ____            ______ ")
  print("/ ___| _ __   __|_   __|  _ _ __   ___ ___   ")
  print("\___ \| '_ \ / _ \| || | | | '_ \ / _ / __|  ")
  print(" ___) | |_) | (_) | || |_| | | | |  __\__ \  ")
  print("|____/| .__/ \___/|_| \__,_|_| |_|\___|___/  ")
  print("      |_|  ")
  
  playlist_link = input("Enter playlist link: ")
  
  playlist = lib_getify.getify(playlist_link)
  playlist.get_tracks()

  for track in playlist.all_tracks:
    track.save_track()
    track.update_file_properities()


if __name__ == '__main__':
  main()
