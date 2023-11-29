import pandas as pd
import os
import hashlib

#定义总体的建议列表
suggestions={}

UPLOAD_FOLDER = 'uploads'
# 敏感字段列表
sensitive_fields = ["username", "email"]
# 范围字段列表
range_fields = ["amount", "pressure","balance","age"]

rules={
    'sensitive_fields':sensitive_fields,
    'range_fields':range_fields
}

def generate_hash(filename):
    # 使用SHA-256哈希函数生成文件的哈希值
    sha256 = hashlib.sha256()
    with open(os.path.join(UPLOAD_FOLDER,filename), 'rb') as f:
        while True:
            data = f.read(65536)  # 64 KB
            if not data:
                break
            sha256.update(data)
    return sha256.hexdigest()

def get_rules():
    return {
            'sensitive_fields':sensitive_fields,
            'range_fields':range_fields
            }

def add_rules(newrules):
    sensitive_fields=newrules['sensitive_fields']
    range_fields=newrules['range_fields']
    rules=newrules
    return {
        'success':True,
        'rules':rules
    }


# 生成建议
def generate_suggestions(header):
    ####添加正则匹配等规则
    header_normalized = header.casefold()  # 不区分大小写
    if header_normalized in [sf.casefold() for sf in sensitive_fields]:
        suggestions[header]='mask'
        return f"建议对 {header} 进行掩盖脱敏处理"
    elif header_normalized in [rf.casefold() for rf in range_fields]:
        suggestions[header]='range'
        return f"建议对 {header} 进行范围化脱敏处理"
    else:
        suggestions[header]='none'
        return f"{header} 字段可以保留原始值"

def make_suggestions(headers):
    # 输出建议
    for header in headers:
        suggestion = generate_suggestions(header)
        print(f"对于字段 '{header}'：{suggestion}")
    return suggestions
