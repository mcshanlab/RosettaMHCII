library(ggplot2)
library(gridExtra)

tag = "/Volumes/8TB_McShan_Drive/RosettaMHCII/database/Historical_Summary/historical_summary"

MIN_YEAR = 1994
MAX_YEAR = 2022
TOTAL_STRUC = 160

data = read.csv(paste0(tag, ".csv"))

plot_bottom <- ggplot(data, aes(x = year)) +
  geom_bar(aes(y = cumulative_sum), stat='identity', fill='white', color='darkblue') + 
  geom_line(aes(y = per_year), stat='identity', color='red') +
  geom_point(aes(y = per_year), stat='identity', color='red') +
  
  scale_x_continuous(limits = c(MIN_YEAR-1,MAX_YEAR+1), expand = c(0, 0)) +
  scale_y_continuous(limits = c(0,TOTAL_STRUC+2), expand = c(0, 0)) +
  
  xlab("Year") + 
  ylab("Cumulative Sum") + 
  ggtitle(paste0("Historical Summary of\nHLA Class II Structures (n = ", TOTAL_STRUC, ")")) +
  scale_x_continuous(labels = as.character(data$year), breaks = data$year) +
  
  theme (
    text=element_text(size=12,  family="Helvetica"),
    plot.title = element_text(hjust = 0.5),
    panel.background = element_rect(fill='white'),
    panel.grid.major.x = element_blank(),
    panel.grid.major.y = element_line(size=0.05,colour='black'),
    axis.text = element_text(size=10),
    axis.ticks.length=unit(0.05, "cm"),
    axis.title.x = element_text(size=12,  family="Helvetica"),
    axis.title.y = element_text(size=12,  family="Helvetica"),
    axis.text.x = element_text(angle=90),
    legend.title=element_blank(),
    legend.position = "none",
    panel.border = element_rect(colour = "black", fill=NA, size=0.5)) 

print("done")
plot_bottom
print(paste0(tag,".png"))
png("historical_summary.png", units="in", width=6, height=5, res = 300)
grid.arrange(plot_bottom)
dev.off()
