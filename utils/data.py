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
