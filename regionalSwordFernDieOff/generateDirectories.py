import json
import os
import yaml
sites = json.load(open('v4.js'))

for i in range(3):
   directoryName = "site.%04d" % i
   if(not os.path.exists(directoryName)):
       os.mkdir(directoryName)
   print(" %s exists? %s" % (directoryName, os.path.exists(directoryName)))
   site = sites[i]
   site["firstReported"] = "2000-01-01"
   site["lastUpdate"] = "2000-01-01"
   site["contact"] = ""
   site["radius"] =  100
   site["area"] = 10
   site["severity"] = 0
   site["notesFile"] = "notes.html"
   siteFileName = os.path.join(directoryName, "site.yaml")
   print("siteFileName: '%s'" % siteFileName)
   siteFile = open(siteFileName, "w")
   yaml.dump(site, siteFile, default_flow_style=False)
   
   

# site.yaml
# firstReported: 2013-10-01
# lastUpdate:  2019-03-01
# contact: Paul Shannon
# radius:  100
# area: 10
# severity: 10
# notesFile: notes.html
# title:  Seward Park Ground Zero
# lat: 47.555474
# lon: -122.248945
# firstReported: 2013-10-01
# lastUpdate:  2019-03-01
# contact: Paul Shannon
# radius:  100
# area: 10
# severity: 10
# notesFile: notes.html
# photoTabs:
#   - title: "Before and After:  2011 2017"
#     url: https://4.bp.blogspot.com/-xpU4_m8AXW0/WhjplTnA2hI/AAAAAAAAX64/n_GNVcM0E1E8xE3EgrJAvjgi5b37nsO6wCLcBGAs/s1600/Screen%2BShot%2B2017-11-24%2Bat%2B7.54.16%2BPM.png
#   - title: Lazarus Fern
#     url: "https://2.bp.blogspot.com/-0u1aT9PEBcI/WqtEkMgaQOI/AAAAAAAAX_0/ailkJiE1w6oCvsCXbcipTvhho6rDiGNWACLcBGAs/s1600/IMG_2057.JPG"
# videoTabs:
#    - title: KING 5 News 2017
#      url: https://www.youtube.com/embed/qtifUa6LTn4



   
