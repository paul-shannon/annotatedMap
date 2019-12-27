library(XML)
file <- "doc.kml"
doc <- xmlParse(file)
str(getNodeSet(doc, "//Docfdsdfument"))

doc = xmlTreeParse(system.file("exampleData", "tagnames.xml", package = "XML"), useInternalNodes = TRUE)
length(getNodeSet(doc, "/doc//b[@status]"))
getNodeSet(doc, "/doc//b[@status='foo']")
