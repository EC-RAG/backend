import os
import sys

# 获取当前脚本所在目录的上级目录
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from vdb import client