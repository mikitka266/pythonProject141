import asyncio
import time
import aiohttp


urls = ['https://kinobase.org/serial/3838-fargo',
        'https://gb.ru/lessons/353423/homework',
        'https://www.youtube.com/watch?v=LTvsgBAbo8Q',
        'https://mail.google.com/mail/u/0/#inbox'
]


async def download(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            text = await response.text()
            filename = 'async_' + url.replace('https//', '').replace('.', '_').replace('/', '') + '.html'
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(text)
            print(f'Downloaded {url} in {time.time() - start_time:.2f} seconds')


async def main():
    tasks = []
    for url in urls:
        task = asyncio.ensure_future(download(url))
        tasks.append(task)
    await asyncio.gather(*tasks)


start_time = time.time()


if __name__ == '__main__':
        for url in urls:
        loop = asyncio(target=download, args=(url,))
        loops.append(loop)
        loops.start()
    
    for loop in loops:
        loop.join()
        