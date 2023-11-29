import csv
import random
import string

# 生成模糊化的AOR值
def anonymize_aor(aor):
    prefix = ''.join(random.choices(string.ascii_uppercase, k=3))
    suffix = ''.join(random.choices(string.digits, k=4))
    return f"{prefix}_{suffix}"

# 打开原始CSV文件
with open('randomdata/event_data.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile, delimiter='|')
    
    # 创建新的CSV文件来保存处理后的数据
    with open('Processed_Event_Export.csv', 'w', newline='') as processed_csvfile:
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(processed_csvfile, fieldnames=fieldnames, delimiter='|')
        
        # 写入CSV文件的表头
        writer.writeheader()
        
        # 处理每一行数据
        for row in reader:
            # 获取原始AOR值
            original_aor = row['AOR']
            
            # 模糊化AOR值
            anonymized_aor = anonymize_aor(original_aor)
            
            # 替换AOR列的值为模糊化后的值
            row['AOR'] = anonymized_aor
            
            # 写入处理后的数据到新的CSV文件
            writer.writerow(row)

print("敏感数据已处理并保存到 Processed_Event_Export.csv 文件中。")
