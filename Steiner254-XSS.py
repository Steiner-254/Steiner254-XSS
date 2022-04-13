from traceback import print_tb
import requests
import threading
import sys
from colorama import Fore, Back, Style


print(
        Fore.YELLOW +
         """
          ____  _       _                ____  ____  _  _   
/ ___|| |_ ___(_)_ __   ___ _ _|___ \| ___|| || |  
\___ \| __/ _ \ | '_ \ / _ \ '__|__) |___ \| || |_ 
 ___) | ||  __/ | | | |  __/ |  / __/ ___) |__   _|
|____/ \__\___|_|_| |_|\___|_| |_____|____/   |_| 

         
                                          [ twitter.com/steiner254 ]
                                          [ github.com/Steiner-254 ]
        """ + Fore.RESET)

print()
print()

def Send_req(url,payload):
    #while url[-1] != '=':
     #   url = url[:-1]
    url = url.replace("=",f"={payload}")

    try:

        res = requests.get(url)
        if payload in res.text:
           print(Fore.RED +'XSS Found   -->','   ' , f"{url}" + Fore.RESET)


    except Exception as e:
        pass

if __name__ == "__main__":
    try:
        payloads = sys.argv[1].strip()
        urls = sys.argv[2].strip()
    except IndexError:
        print("[-] Usage: python3 %s <payloads> <urls>" % sys.argv[0])
        print("[-] Example: python3 %s payload.txt url.txt" % sys.argv[0])
        sys.exit(-1)

payloads = open(f'{payloads}', 'r', encoding='utf-8')
urls = open(f'{urls}', 'r', encoding='utf-8')
payloads = payloads.readlines()
for payload in payloads:
    for url in urls:
        url = url.strip('\n')
        payload = payload.strip('\n')
        threading.Thread(target=Send_req,args=(url,payload,)).start()
