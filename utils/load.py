import os
import sys
import requests
import tarfile

def get_tag():
    """
    获取当前前端仓库最新的tag
    """
    url = 'https://api.github.com/repos/EC-RAG/frontend/tags'
    response = requests.get(url)
    tags = response.json()
    # print(tags)
    try:
        if tags:
            return tags[0]['name']
    except Exception as e:
        return 'v1.0.2'

def download_frontend(tag):
    '''
    下载前端文件
    ----
    tag: str  
        前端版本号
    '''
    url = f'https://github.com/EC-RAG/Frontend/releases/download/{tag}/frontend.tar.gz'
    filename = 'frontend.tar.gz'
    with requests.get(url, stream=True) as r:
        r.raise_for_status()  # 检查是否成功
        with open(filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    # 解压到./frontend目录
    with tarfile.open(filename, 'r:gz') as tar:
        tar.extractall(path='./frontend')
    # 删除压缩包
    os.remove(filename)
    # 保存当前版本号
    with open('./frontend/_version', 'w') as f:
        f.write(tag)


def check_frontend():
    if os.path.exists('/frontend'):
        # 如果存在前端目录，检查版本号
        with open('/frontend/_version', 'r') as f:
            version = f.read()
        tag = get_tag()
        if tag != version:
            # 如果版本号不同，下载新版本
            download_frontend(tag)
    else:
        # 如果不存在前端目录，下载最新版本
        tag = get_tag()
        download_frontend(tag)