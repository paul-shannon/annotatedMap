library(yaml)
x <- yaml.load(readLines("doc4.raw"))

coi <- c("Date", "Comments", "lat", "lon")
x2 <- lapply(x, function(myList) myList[coi])
tbl <-  data.frame(matrix(unlist(x2), nrow=length(x2), byrow=T),stringsAsFactors=FALSE)
colnames(tbl) <- coi
rownames(tbl) <- names(x2)
head(tbl)

dead.numbers <- lapply(tbl$Comments, function(s) sum(as.integer(str_match_all(s, "(\\d+)")[[1]][,1])))
tbl$deadCount <- unlist(dead.numbers)
lapply(tbl, class)
save(tbl, file="alSmithsCleanedDataFromKmlFile.RData")

