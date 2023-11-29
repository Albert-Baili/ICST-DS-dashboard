import random
import time
import csv

# 定义传感器的数量和数据生成间隔
num_sensors = 5
data_interval = 1  # 每隔1秒生成一组数据

# 打开CSV文件以保存数据
with open('industrial_data.csv', 'w', newline='') as csvfile:
    fieldnames = ['时间', '传感器ID', '温度（摄氏度）', '湿度（%）', '压力（PSI）']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    # 模拟数据生成
    for i in range(100):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        for sensor_id in range(1, num_sensors + 1):
            temperature = round(random.uniform(20, 30), 2)  # 模拟温度数据
            humidity = round(random.uniform(40, 60), 2)    # 模拟湿度数据
            pressure = round(random.uniform(10, 20), 2)    # 模拟压力数据

            # 写入CSV文件
            writer.writerow({
                '时间': timestamp,
                '传感器ID': sensor_id,
                '温度（摄氏度）': temperature,
                '湿度（%）': humidity,
                '压力（PSI）': pressure
            })

        time.sleep(data_interval)  # 控制数据生成的时间间隔
