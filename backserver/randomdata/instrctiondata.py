import csv
import random
import time

# 生成随机SCADA数据包的函数
def generate_random_scada_data(num_packets):
    scada_data = []
    for _ in range(num_packets):
        source = f"传感器_{random.randint(1, 10)}"
        destination = "SCADA服务器"
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        temperature = round(random.uniform(20, 30), 2)
        pressure = round(random.uniform(80, 120), 2)
        flow_rate = round(random.uniform(40, 60), 2)
        device_id = random.randint(1000, 9999)
        control_command = random.choice(["打开阀门", "关闭阀门", "切换状态"])
        device_status = random.choice(["在线", "离线"])
        
        scada_data.append([source, destination, timestamp, temperature, pressure, flow_rate, device_id, control_command, device_status])
    
    return scada_data

# 定义要生成的SCADA数据包数量
num_packets_to_generate = 50

# 生成SCADA数据包
scada_data = generate_random_scada_data(num_packets_to_generate)

# 将SCADA数据包写入CSV文件
with open('scada_data.csv', 'w', newline='') as csvfile:
    fieldnames = ['来源', '目标', '时间戳', '温度（摄氏度）', '压力（PSI）', '流量（L/min）', '设备ID', '控制命令', '设备状态']
    writer = csv.writer(csvfile)
    
    # 写入CSV文件的表头
    writer.writerow(fieldnames)
    
    # 写入SCADA数据包
    for packet in scada_data:
        writer.writerow(packet)

print(f"{num_packets_to_generate} 个随机SCADA数据包已生成并写入 scada_data.csv 文件。")
