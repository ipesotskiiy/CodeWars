# from preloaded import send_request
import asyncio


async def request_manager(n: int) -> str:
    tasks = []
    count_iteration = 0

    for iteration in range(n):
        # tasks.append(asyncio.create_task(send_request()))
        count_iteration += 1
        if count_iteration == n:
            return ''.join(await asyncio.gather(*tasks))