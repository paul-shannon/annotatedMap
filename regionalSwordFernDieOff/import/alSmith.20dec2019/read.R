f <- "AlSmith_SwordFern_Survey_12-20-19.txt"
tbl <- read.table(f, sep="\t", header=TRUE, as.is=TRUE, nrow=-1, fill=TRUE, quote=NULL)
dim(tbl)
colnames(tbl)[11:14] <- c("status", "notes", "lon", "lat")
coi <- c("Park.Location", "Address", "Date", "status", "lat", "lon", "notes")
tail(subset(tbl, status==2))[, coi]
