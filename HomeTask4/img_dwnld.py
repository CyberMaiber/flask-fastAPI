# Для выбора способа скачивания меняем переменную fnc_num
# Если запуск с аргументами, то первый аргумент это значение fnc_num, затем через пробел адреса.

import time, sys, threading, requests
from multiprocessing import Process, Pool
import asyncio, aiohttp, aiofiles
urls = [
    'https://upload.wikimedia.org/wikipedia/commons/thumb/a/aa/Astra_Linux_Fly_Desktop.png/1200px-Astra_Linux_Fly_Desktop.png',
    'https://www.iphones.ru/wp-content/uploads/2022/09/BC56F70A-7D16-44FB-A166-10C457932611.png',
    'https://reshenie-soft.ru/modules/dblog/rtl/news/3/1/astra.png',
    'https://spbit.ru/uploads/Article/198/AL23_1670849354.jpg',
    'https://i.ytimg.com/vi/SEiBkpZffuw/sddefault.jpg',
    'https://i.ytimg.com/vi/Ug1cQadP1QI/maxresdefault.jpg',
    'https://www.iphones.ru/wp-content/uploads/2019/11/astra_linux_common-43.jpg',
    'https://www.cischool.ru/wp-content/uploads/2018/07/1473429874_3394cf7e12c8.png',
    'https://3dnews.ru/assets/external/illustrations/2020/05/14/1010971/astralinux1405-1.png',
    'https://astralinux.ru/upload/iblock/bfb/zrrfl448a1vvltdomqyw41g065mcsiwl.svg',
    'https://img.ixbt.site/live/topics/preview/00/04/20/08/d814441b4b.png',
    'https://astralinux.ru/upload/iblock/971/40in5lgsvfo0w67bu6ddt7l4sljiofue.png'
    ]

# Нет прямого доступа в интернет, пришлось костыль запилить :)
# urls = [ 
#     'http://127.0.0.1:5000/static/img/bot1.jpg',
#     'http://127.0.0.1:5000/static/img/bot2.jpg',
#     'http://127.0.0.1:5000/static/img/bot3.jpg',
#     'http://127.0.0.1:5000/static/img/shp1.jpg',
#     'http://127.0.0.1:5000/static/img/shp2.jpg',
#     'http://127.0.0.1:5000/static/img/shp3.jpg',
#     'http://127.0.0.1:5000/static/img/kur1.jpg',
#     'http://127.0.0.1:5000/static/img/kur2.jpg',
#     'http://127.0.0.1:5000/static/img/kur3.jpg'
#     ]

def download(img_url:str):
    start_time = time.time()
    response = requests.get(img_url)
    filename = img_url.split('/')[-1]
    with open(filename, "wb") as f:
        f.write(response.content)
    print(f"Downloaded {img_url} in {time.time()-start_time:.3f}seconds")

async def download_(img_url:str):
    start_time = time.time()
    async with aiohttp.ClientSession() as session:
        async with session.get(img_url) as response:
            if response.status == 200:
                filename = img_url.split('/')[-1]
                f = await aiofiles.open(filename, mode='wb')
                await f.write(await response.read())
                await f.close()
    print(f"Downloaded {img_url} in {time.time()-start_time:.3f}seconds")

def threading_def(urls_in):
    print('Скачивание с помощью многопоточности.')
    threads = []
    all_start_time = time.time()
    for url in urls_in:
        thread = threading.Thread(target=download, args=[url])
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    print(f"Downloaded all urls in {time.time()-all_start_time:.3f}seconds")


def multiprocessing_def(urls_in):
    print('Скачивание с помощью многопроцессорности.')
    processes = []
    all_start_time = time.time()
    for url in urls_in:
        process = Process(target=download, args=[url])
        processes.append(process)
        process.start()
    for process in processes:
        process.join()
    print(f"Downloaded all urls in {time.time()-all_start_time:.3f}seconds")

async def asynchron(urls_in):
    tasks = []
    for url in urls_in:
        task = asyncio.ensure_future(download_(url))
        tasks.append(task)
    await asyncio.gather(*tasks)

def asynchron_def(urls_in):
    print('Скачивание с помощью асинхронности.')
    all_start_time = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asynchron(urls_in))
    print(f"Downloaded all urls in {time.time()-all_start_time:.3f}seconds")

if __name__ == '__main__':
    fnc_num = 3 #Переменная для определения с помощью чего скачиваем 1-многопоточность,2-многпроцессорность,3-асинхронность
    funcs = {
        1:threading_def,
        2:multiprocessing_def,
        3:asynchron_def
    }
    if len(sys.argv) > 2:
        funcs[int(sys.argv[1])](sys.argv[2:])
    else:
        funcs[fnc_num](urls)


