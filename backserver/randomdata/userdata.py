import csv
import random

# 生成随机用户数据的函数
def generate_random_user_data(num_users):
    user_data = []
    for _ in range(num_users):
        user_id = random.randint(1000, 9999)
        username = f"user_{user_id}"
        age = random.randint(18, 65)
        email = f"{username}@example.com"
        balance = round(random.uniform(100, 10000), 2)
        user_data.append([user_id, username, age, email, balance])
    
    return user_data

# 定义要生成的用户数量
num_users_to_generate = 100

# 生成用户数据
user_data = generate_random_user_data(num_users_to_generate)

# 将用户数据写入CSV文件
with open('user_data.csv', 'w', newline='') as csvfile:
    fieldnames = ['User ID', 'Username', 'Age', 'Email', 'Balance']
    writer = csv.writer(csvfile)
    
    # 写入CSV文件的表头
    writer.writerow(fieldnames)
    
    # 写入用户数据
    for user in user_data:
        writer.writerow(user)

print(f"{num_users_to_generate} 个随机用户数据已生成并写入 user_data.csv 文件。")
