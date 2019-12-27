# status: abandoned for now
from xml.etree import ElementTree as etree
filename = "doc.kml"
xmlDoc = etree.parse(filename)
len(xmlDoc.findall("Folder"))  # /Placemark"))
len(placeMarks)

from pykml import parser

with open(filename) as f:
    doc.parser.parse(f)
    
