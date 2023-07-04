Async Request Manager | Don't let server down!

Note: this kata is slightly extended version of this kata: https://www.codewars.com/kata/62c702489012c30017ded374

Feel free to check it out first if you wish or if you have problems with solving this little bit harder one.

Original requirements:

Your task is it to implement a coroutine which sends n requests and concats the returned strings of each response to one string.

A request can be made by invoking the prebuild coro send_request. When invoked, the coro sleeps for 1 sec and then returns a single character.

Your overall task is to implement an async request_manager which completes all n requests in under 2.1 sec

Aditional requirement:

Async gives you great power. But it turns out that with great power comes great responsibility. Resource you're requesting for is a pretty weak little... smart toaster? Anyway, DON'T LET SERVER DOWN! under the almighty onslaught of hundreds of simultaneous requests.

TIP: The "server" can handle up to 150 requests at the same time (concurrently).

Note: The kata has a really thin gap between "too fast" and "too slow". But with the right setup, you're guaranteed to hit the right time without letting the "server" down.

Summary:

Implement a coro request_manager which sends and processes fake requests

It accepts the parameter n which represents the amount of requests that should be made
Requests have to be made with send_request

send_request is a preloaded coroutine : (coro) send_request() -> str

It takes 1 sec until a character is returned to the caller

The waiting time is implemented via asyncio.sleep
Characters returned by send_request have to be concat to one string

That string is then returned by your request_manager

The characters in the string need to be ordered, so that the character returned by the first request is at index 0, the character returned by the second request is at index 1 etc.

Your request_manager has 2.1 sec to start & process all n requests and to return the desired string

150 simultaneous requests is the threshold. If in the process of handling them the "server" receives one hundred and fifty-first request in the queue - the game is over.

Solve the kata, and use your asynchronous power wisely, my friend.

P.S. (Not a bug, but a feature): if the toaster receives too many requests, it will actually overheat and thus fail not only the test in which it received an overheat, but also all subsequent ones automaticaly. Be gentle with him, in short ;)
