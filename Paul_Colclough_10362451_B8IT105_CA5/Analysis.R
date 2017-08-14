setwd('C:/Users/Paul/Desktop/CA5')


# load in the active days CSV file and set col headings
df <- read.csv('changes.csv')
colnames(df)
fix(df)
attach(df)

#Days of the week analysis
day <- df$Day

dayFactor <- as.factor(day)
dayord <- c("Mon", "Tue", "Wed", "Thu", "Fri")
dayFactor <- factor(dayFactor, levels = dayord)

png(file = 'chart_commits_day.png')

barplot(prop.table(table(dayFactor)))

dev.off()


##Days of the week analysis
hour <- df$Hour

hourFactor <- as.factor(hour)

png(file = 'chart_commits_hour.png')

barplot(prop.table(table(hourFactor)), xlab="Hours of the day")

dev.off()


#Author analysis
author <- df$Author


png(file = 'chart_commits_author.png')

authorFactor <- as.factor(author)

barplot(prop.table(table(authorFactor)),las=2)

dev.off()