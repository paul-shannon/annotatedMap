f.orig <- "Text7Oct2015.csv"
f <- "text.tsv"
read.table(file=f, header=TRUE, as.is=TRUE, sep="\t", skip=0, nrow=-11)
tbl <- read.table(file=f, header=TRUE, as.is=TRUE, sep=",", nrow=3, fill=TRUE)
dim(tbl)
tbl[, 1:3]
