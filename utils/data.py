import numpy as np

def dicts_to_markdown_table(data):
    if not data:
        return ""

    # 获取表头
    headers = list(data[0].keys())
    header_line = "| " + " | ".join(headers) + " |"
    separator_line = "| " + " | ".join(["---"] * len(headers)) + " |"

    # 构建每一行数据
    rows = []
    for row in data:
        row_line = "| " + " | ".join(str(row.get(h, "")) for h in headers) + " |"
        rows.append(row_line)

    return "\n".join([header_line, separator_line] + rows)


def convert_array_to_list(data):
    if isinstance(data, dict):  # 如果是字典，递归遍历每个键值对
        return {key: convert_array_to_list(value) for key, value in data.items()}
    elif isinstance(data, list):  # 如果是列表，遍历列表中的每个元素
        return [convert_array_to_list(item) for item in data]
    elif isinstance(data, np.ndarray):  # 如果是 numpy 数组，转换为列表
        return data.tolist()
    else:
        return data  # 否则，返回原始值