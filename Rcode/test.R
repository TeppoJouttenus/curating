require(jsonlite)
fqlQuery = "select share_count,like_count,comment_count from link_stat where url=\""
url = "http://www.theguardian.com/world/2014/mar/03/ukraine-navy-officers-defect-russian-crimea-berezovsky"
queryUrl = paste0("http://graph.facebook.com/fql?q=", fqlQuery, url, "\"")  #ignoring the callback part
lookUp <- URLencode(queryUrl)  #What do you think this does?
lookUp
rd <- readLines(lookUp, warn = "F")

dat <- fromJSON(rd)
dat$data$share_count
