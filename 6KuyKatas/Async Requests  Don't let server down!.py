import asyncio
from preloaded import send_request


async def gather_responses_bulk(n: int) -> str:
    res = await asyncio.gather(*[send_request() for _ in range(n)])
    return ''.join(res)


async def request_manager(n: int) -> str:
    output = ''
    while n > 0:
        req_count = 150 if n >= 150 else n
        output += await gather_responses_bulk(req_count)
        n -= req_count

    return ''.join(output)
