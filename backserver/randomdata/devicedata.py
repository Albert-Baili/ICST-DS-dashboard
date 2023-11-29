import csv
import random
import time
from datetime import datetime

# 生成设备状态数据
def generate_device_status(device_count, total_entries):
    devices = [f"Device-{i+1}" for i in range(device_count)]
    statuses = ["正常运行", "故障", "维护中", "待机"]
    data = []

    for _ in range(total_entries):
        device = random.choice(devices)
        status = random.choice(statuses)
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        data.append([device, timestamp, status])

    return data

# 保存数据到CSV文件
def save_to_csv(data, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['设备ID', '时间戳', '状态'])
        writer.writerows(data)

if __name__ == "__main__":
    device_count = 5  # 设备数量
    total_entries = 100  # 生成的总条目数

    device_status_data = generate_device_status(device_count, total_entries)
    save_to_csv(device_status_data, 'device_status.csv')

    print(f"{total_entries} 条设备状态数据已生成并保存到 device_status.csv 文件中。")
