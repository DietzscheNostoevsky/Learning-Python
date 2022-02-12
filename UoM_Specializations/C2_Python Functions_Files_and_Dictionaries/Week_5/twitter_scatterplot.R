path <- "/Users/saurabhkumarsingh/Documents/GitHub/Learning_python/UoM_Specializations/C2_Python Functions_Files_and_Dictionaries/Week_5/resulting_data.csv"
content <- read.csv(path)

print(content)

plot(content$Net.Score, content$Number.of.Retweets,
     pch = 19,         # Solid circle
     cex = 1.5,        # Make 150% size
     col = "#cc0000",  # Red
     main = "Twitter Sentiment Classifier",
     xlab = "Net Score",
     ylab = "Number of Retweets")
     
     
     
