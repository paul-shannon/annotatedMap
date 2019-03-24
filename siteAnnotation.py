# -*- coding: utf-8 -*-
#
# SiteAnnotation.py: a class to capture, and render into HTML, text, photos and video describing
#   a location on a google map
#
#------------------------------------------------------------------------------------------------------------------------
import yaml
from yattag import *
import pdb
import os
#------------------------------------------------------------------------------------------------------------------------
class SiteAnnotation:

   directoryAbsolutePath = None   # where the annotation (site.yaml, notes.html, etc) can be found
   title = "",
   lat = 0
   lon = 0
   firstReported = None
   lastUpdate = None
   contributedBy = None
   radius = 0         # a map metric, approximate, used only for rendering markers on the map
   area = 0           # in acres
   severity = 0       # informal scale of 0 - 10
   notesFile = ''
   photoTabs = []
   videoTabs = []

   def __init__(self, yamlFile):
       assert(os.path.exists(yamlFile))
       self.directoryAbsolutePath = os.path.dirname(yamlFile)
       info = yaml.load(open(yamlFile))
       keys = list(info.keys())
       assert(self.validAnnotation(info))
       self.title = info["title"]
       self.firstReported = info["firstReported"]
       self.lastUpdate = info["lastUpdate"]
       self.contact = info["contact"]
       self.lat = info["lat"]
       self.lon = info["lon"]
       self.area = info["area"]
       self.radius = info["radius"]
       self.severity = info["severity"]
       self.notesFile = info["notesFile"]
       if("photoTabs" in keys):
          self.photoTabs = info["photoTabs"]
       if("videoTabs" in keys):
          self.videoTabs = info["videoTabs"]

     # a draft version only.  better error messages and consistent return strategy needed
   def validAnnotation(self, info):
      keys = list(info.keys())
      requiredKeys = ['title', 'lat', 'lon', 'firstReported', 'lastUpdate', 'contact',
                      'radius', 'area', 'severity', 'notesFile']
      if(not all([requiredKey in keys for requiredKey in requiredKeys])):
          print("invalid yaml file, missing required keys:")
          print(list(set(requiredKeys) - set(["title"])))
          return(False)
      if("photoTabs" in keys):
          photosInfo = info["photoTabs"]
          for photoInfo in photosInfo:
              photoInfoFields = list(photoInfo.keys())
              assert("title" in photoInfoFields)
              assert("url" in photoInfoFields)
      if("videoTabs" in keys):
          videosInfo = info["videoTabs"]
          for videoInfo in videosInfo:
              videoInfoFields = list(videoInfo.keys())
              assert("title" in videoInfoFields)
              assert("url" in videoInfoFields)
      return(True)

   def getTitle(self):
       return(self.title)

   def getLat(self):
       return(self.lat)

   def getLon(self):
       return(self.lon)

   def getRadius(self):
       return(self.radius)

   def getSeverity(self):
       return(self.severity)

   def getNotesFileName(self):
       return(self.notesFile)

   def getPhotoTabs(self):
       return(self.photoTabs)

   def getVideoTabs(self):
       return(self.videoTabs)




