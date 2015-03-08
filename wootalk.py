#!/usr/bin/env python3.3

from time import time
import json
import re
from multiprocessing.pool import ThreadPool
from time import time, sleep

import requests
from websocket import create_connection, WebSocketTimeoutException
from colorama import Fore

def bot(i):
    header = {
     "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.76 Safari/537.36",
     "Origin": "https://wootalk.today",
     "Connection": "Upgrade"
    }
    wss = create_connection("wss://wootalk.today/websocket", header= header)
    update = wss.accept()
    # new = wss.bind('new_message')

# GET wss://wootalk.today/websocket HTTP/1.1
# Host: wootalk.today
# Connection: Upgrade
# Pragma: no-cache
# Cache-Control: no-cache
# Upgrade: websocket
# Origin: https://wootalk.today
# Sec-WebSocket-Version: 13
# DNT: 1
# User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.76 Safari/537.36
# Accept-Encoding: gzip, deflate, sdch
# Accept-Language: zh-TW,zh;q=0.8,en-US;q=0.6,en;q=0.4
# Cookie: _wootalk_session=22d6d14aa852faa282b90c779d703b72; _ga=GA1.2.2127744561.1425696177; _gat=1
# Sec-WebSocket-Key: bqVyoTtb+pORLLQHQpp6Sg==
# Sec-WebSocket-Extensions: permessage-deflate; client_max_window_bits


    print(i)
    message = wss.recv()
    print(message)
    while True:
        message = ws.recv()
        print("2")
        try:
            message = ws.recv()
        except WebSocketTimeoutException:
            continue

def main():
    # res = requests.get('https://wootalk.today/websocket')
    # puts(res)
    # clear text color
    # print(Fore.RESET)
    # file_name =str(int(round(time())))
    # myfile = open('logs/'+file_name+'.log', 'a')
    global first
    first = None
    # global second
    # second = None
    # global is_disconnect
    # is_disconnect = False

    # create a pool
    pool = ThreadPool(2)
    # start first user
    pool.apply_async(bot, ('0'))
    sleep(3)
    pool.apply_async(bot, ('1'))
    # start second user after one second,
    # so they won't match together
    # pool.apply_async(bot, ('1',myfile))

    # close pool and wait for them to disconnect
    pool.close()
    pool.join() 
    # myfile.close()
    
    # ws.settimeout(1)





if __name__ == '__main__':
    while True:
        main()
