import pandas as pd
import matplotlib.pyplot as plt
import requests
from io import StringIO
import numpy as np

# 提供的CSV文件的URL
url = "https://data.weather.gov.hk/weatherAPI/cis/csvfile/HKA/2024/daily_HKA_RF_2024.csv"

# 从URL下载CSV文件
response = requests.get(url)
response.raise_for_status()  # 确保请求成功

# 将下载的内容转换为一个可读的CSV格式
csv_data = StringIO(response.text)

# 使用pandas读取CSV数据，跳过前两行的说明，并尝试不同的编码
data = pd.read_csv(csv_data, skiprows=2, encoding='ISO-8859-1')  # 尝试使用ISO-8859-1编码

# 查看数据的列名，确保读取正确
print(data.columns)

# 重命名列名以处理乱码问题
data.columns = ['Year', 'Month', 'Day', 'Value', 'Data Completeness']

# 检查并删除 'Month' 和 'Day' 列中的缺失值
data = data.dropna(subset=['Month', 'Day'])

# 将'Month'和'Day'列转换为整数类型，确保没有小数点
data['Month'] = data['Month'].astype(int).astype(str).str.zfill(2)  # 转换为字符串并填充为两位
data['Day'] = data['Day'].astype(int).astype(str).str.zfill(2)      # 转换为字符串并填充为两位

# 替换特殊符号
data['Value'] = data['Value'].replace({
    '***': np.nan,  # 没有数据
    '#': np.nan,    # 数据不完整
    'Trace': 0.05   # Trace表示少于0.1毫米的降雨，假设为0.05毫米
}).astype(float)

# 创建一个新的日期列
data['Date'] = pd.to_datetime('2024-' + data['Month'] + '-' + data['Day'], format='%Y-%m-%d')

# 排序数据
data = data.sort_values('Date')

# 绘制降雨量数据图
plt.figure(figsize=(12, 6))
plt.plot(data['Date'], data['Value'], marker='o', linestyle='-')

# 设置图表的标题和坐标轴名称
plt.title('Total Rainfall (mm) - Hong Kong International Airport')
plt.xlabel('Date')
plt.ylabel('Value (mm)')

# 显示网格和旋转x轴标签
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

# 显示图表
plt.show()
