import csv
import random
import time

# 随机生成SCADA事件数据的函数
def generate_random_scada_event(event_id):
    event_time = f"2017-05-{random.randint(1, 31)} {random.randint(0, 23)}:{random.randint(0, 59)}:{random.randint(0, 59)}"
    scada_category = random.choice(["Power Outage", "Voltage Fluctuation", "Overload", "Equipment Failure"])
    aor = f"Operator_{random.randint(1, 5)}"
    priority_code = random.randint(1, 8)
    substation = f"Substation{random.randint(100, 999)}"
    device_type = random.choice(["Transformer", "Circuit Breaker", "Generator", "Switchgear"])
    event_message = f"Event {event_id} occurred at {event_time} - {scada_category} detected."
    return [event_id, event_time, scada_category, aor, priority_code, substation, device_type, event_message]

# 定义要生成的事件数量
num_events_to_generate = 100

# 生成事件数据
event_data = []
for event_id in range(1, num_events_to_generate + 1):
    event = generate_random_scada_event(event_id)
    event_data.append(event)

# 将事件数据写入CSV文件
with open('event_data.csv', 'w', newline='') as csvfile:
    fieldnames = ['EventId', 'EventTimeStamp', 'SCADA_Category', 'AOR', 'Priority_Code', 'Substation', 'DeviceType', 'event_message']
    writer = csv.writer(csvfile, delimiter='|')
    
    # 写入CSV文件的表头
    writer.writerow(fieldnames)
    
    # 写入事件数据
    for event in event_data:
        writer.writerow(event)

print(f"{num_events_to_generate} 个随机SCADA事件数据已生成并写入 Event_Export_082217.csv 文件。")
