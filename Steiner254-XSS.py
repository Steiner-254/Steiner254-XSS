import requests
import threading
from colorama import Fore, Back, Style


print(
        Fore.BLUE +
         """
 ____  _       _                ____  ____  _  _       __  ______ ____  
/ ___|| |_ ___(_)_ __   ___ _ _|___ \| ___|| || |      \ \/ / ___/ ___| 
\___ \| __/ _ \ | '_ \ / _ \ '__|__) |___ \| || |_ _____\  /\___ \___ \ 
 ___) | ||  __/ | | | |  __/ |  / __/ ___) |__   _|_____/  \ ___) |__) |
|____/ \__\___|_|_| |_|\___|_| |_____|____/   |_|      /_/\_\____/____/ 
                                                                        
  
     
                                          [ twitter.com/steiner254 ]
                                          [ github.com/Steiner-254 ]
        """ + Fore.RESET)

print()
print()
file = open('url.txt','r')
payloads = open('payloads.txt','r')
def Send_req(url,payload):
    #while url[-1] != '=':
     #   url = url[:-1]
    url = url.replace("=",f"={payload}")

    try:

        res = requests.get(url)
        if payload in res.text:
           print(Fore.GREEN +'XSS Found   -->','   ' , f"{url}" + Fore.RESET)


    except Exception as e:
        pass
file = file.readlines()
for payload in payloads:
    for url in file:
        url = url.strip('\n')
        payload = payload.strip('\n')
        threading.Thread(target=Send_req,args=(url,payload,)).start()
