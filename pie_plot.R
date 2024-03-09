# 加载所需的包
library(ggplot2)

# 获取输入文件名和输出路径
args <- commandArgs(trailingOnly = TRUE)
file_name <- args[1]
output_file <- args[2]

# 读取数据
data <- read.table(file_name, header = FALSE)

# 将数据转换为数据框
df <- data.frame(
  category = factor(data$V2, levels = unique(data$V2)),
  frequency = data$V1
)

# 计算每个类别的百分比
df$percentage <- df$frequency / sum(df$frequency) * 100

# 根据百分比降序排序
df <- df[order(-df$percentage), ]

# 绘制所有数据的饼图
pie_plot_all <- ggplot(df, aes(x = "", y = percentage, fill = category)) +
  geom_col(color = "#696969") + 
  coord_polar("y", start = 0) +
  theme_void() +
  theme(legend.position = "bottom") +
  labs(title = "Virus Family (All)")

# 绘制占比前10的饼图
top_10 <- df[1:10, ]
pie_plot_top_10 <- ggplot(top_10, aes(x = "", y = percentage, fill = category)) +
  geom_col(color = "#696969") + 
  coord_polar("y", start = 0) +
  theme_void() +
  theme(legend.position = "right") +
  labs(title = "Virus Family (Top 10)")

# 使用分面方法将两个饼图放在一张图片里面
combined_plot <- cowplot::plot_grid(pie_plot_all, pie_plot_top_10, nrow = 1)

# 保存组合图为PDF格式
ggsave(output_file, plot = combined_plot, width = 12, height = 6)
