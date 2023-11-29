import re

# 定义正则表达式
regex_patterns = {
    "email": r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+",
    "phone": r"\b\d{3}[-.]?\d{3}[-.]?\d{4}\b",
    "date": r"\b\d{4}[-/]\d{2}[-/]\d{2}\b"
}

def classify_data(data, patterns):
    classified_data = {"email": [], "phone": [], "date": [], "unknown": []}
    for item in data:
        matched = False
        for data_type, pattern in patterns.items():
            if re.search(pattern, item):
                classified_data[data_type].append(item)
                matched = True
                break

        if not matched:
            classified_data["unknown"].append(item)

    return classified_data

data_samples = ["example@example.com", "123-456-7890", "2023-11-21", "unknown data"]

classified_results = classify_data(data_samples, regex_patterns)

print(classified_results)
