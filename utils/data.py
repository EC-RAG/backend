import numpy as np
from langchain.text_splitter import RecursiveCharacterTextSplitter
import datetime

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
        return convert_array_to_list(data.tolist())
    elif isinstance(data, datetime.date):  # 如果是日期
        return data.strftime("%Y-%m-%d")  # 转换为字符串格式
    else:
        return data  # 否则，返回原始值
    
def text_split(content: str, chunk_size: int = 500, chunk_overlap: int = 50) -> list:
    """
    将文本分割成多个块
    :param content: 要分割的文本
    :param chunk_size: 每个块的大小
    :param chunk_overlap: 块之间的重叠大小
    :return: 分割后的文本块列表
    """
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", "。", ".", "！", "？", ",", "，", " "]
    )
    docs = text_splitter.create_documents([content])
    chunks = [doc.page_content for doc in docs]
    return chunks

def dict_to_list(data: dict, include:list) -> list:
    """
    将字典转换为列表
    :param data: 要转换的字典
    :param include: 包含的键列表
    :return: 转换后的列表
    """
    return [{key: data.get(key)[index] for key in include} for index in range(len(data.get(include[0])))]
