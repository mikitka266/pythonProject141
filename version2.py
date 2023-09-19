import time
from multiprocessing import Process

urls = ['https://kinobase.org/serial/3838-fargo',
        'https://gb.ru/lessons/353423/homework',
        'https://www.youtube.com/watch?v=LTvsgBAbo8Q',
        'https://mail.google.com/mail/u/0/#inbox'
]


def download(url):
    response = requests.get(url)
    filename = 'multiproc_' + url.replace('http://', '').replace('.', '_').replace('/', '') + '.html'
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(response.text)
    print(f'Downloaded {url} in {time.time() - start_time:.2f} seconds')


processes = []
start_time = time.time()


if __name__ == '__main__':
    for url in urls:
        process = Process(target=download, args=(url,))
        processes.append(process)
        process.start()
    
    for process in processes:
        process.join()
        