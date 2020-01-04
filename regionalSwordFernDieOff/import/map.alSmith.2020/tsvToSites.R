library(yaml)
f <- "../alSmith.20dec2019/AlSmith_SwordFern_Survey_12-20-19.txt"
tbl <- read.table(f, sep="\t", header=TRUE, as.is=TRUE, nrow=-1, fill=TRUE, quote=NULL)
dim(tbl)
colnames(tbl)[11:14] <- c("status", "notes", "lon", "lat")
coi <- c("Park.Location", "Address", "Date", "status", "lat", "lon", "notes")
tbl <- subset(tbl, status != 0)
dim(tbl)
tbl <- subset(tbl, nchar(Park.Location) > 0)
dim(tbl)
tail(subset(tbl, status==2))[, coi]

#rows <- seq_len(3)
rows <- seq_len(nrow(tbl))
for(row in rows){
   x <- list()
   data <- as.list(tbl[row,])
   x$area <- 0
   x$color <- "blue"
   x$borderColor <- "blue"
   x$contact <- "Al Smith"
   firstReported <- gsub('"', '', data$Date)
   x$firstReported <- firstReported
   x$lastUpdate <- firstReported
   x$lat <- data$lat
   x$lon <- data$lon
   x$notesFile <- ""
   x$radius <- 10
   x$severity <- data$status
   x$text <- paste(data$Comments, data$Address)
   parkLocation <- gsub("'", "", data$Park.Location)
   parkLocation <- gsub('"', '', parkLocation)
   comments <- gsub("'", "", data$Comments)
   comments <- gsub('"', '', comments)
   x$title <- paste0(parkLocation, ": ", comments)
   x$type <- "rectangle"
   dir.name <- sprintf("site.%04d", row + 2000)  # esite.2001, 2 indicates al smith
   if(!file.exists(dir.name))
      dir.create(dir.name)
   path <- file.path(dir.name, "site.yaml")
   write_yaml(x, path)
   } # for row
