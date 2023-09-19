import version1
import threading
import time


urls = ['https://kinobase.org/serial/3838-fargo',
        'https://gb.ru/lessons/353423/homework',
        'https://www.youtube.com/watch?v=LTvsgBAbo8Q',
        'https://mail.google.com/mail/u/0/#inbox'
]


def download(url):
    response = requests.get(url)
    filename = 'thread_' + url.replace(' https://', '').replace('.','_') + '.html'
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(response.text)
    print(f'Downloaded {url} in {time.time() - start_time:.2f} seconds')


threads = []
start_time = time.time()

for url in urls:
    thread = threading.Thread(target=download, args=[url])
    threads.append(thread)
    thread.start()


for thread in threads:
    thread.join()
