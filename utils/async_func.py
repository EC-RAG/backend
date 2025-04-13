import asyncio
from concurrent.futures import ThreadPoolExecutor

executor = ThreadPoolExecutor()

# 将同步函数包装为异步
async def run_sync(func, *args):
    loop = asyncio.get_running_loop()
    return await loop.run_in_executor(executor, lambda: func(*args))