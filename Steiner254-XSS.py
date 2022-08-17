import sys
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
          
def get_url():
    file = open('url.txt','r')
    try:    
        n = len(sys.argv)
        if n == 1:
            file = file.readlines()    # get url from file
            for payload in payloads:
                for url in file:
                    url = url.strip('\n')
                    payload = payload.strip('\n')
                    threading.Thread(target=Send_req,args=(url,payload,)).start()
        elif n == 3:
            if "--url" or "-u" in sys.argv[1]:
                url = sys.argv[2]     # get url from terminal
                for payload in payloads:
                    payload = payload.strip('\n')
                    threading.Thread(target=Send_req,args=(url,payload,)).start()
            else:
                usage()
        else:
            usage()
    except KeyboardInterrupt:
        print("\nKeyboard interrupted. \nExiting...")
        sys.exit(0)

def usage():
    print("""Usage: \n
          cd Steiner254-XSS \n
          Add list of your target urls containing parameters in url.txt \n
          python3 Steiner254-XSS.py \n
          OR \n
          python3 Steiner254-XSS.py --url http://testphp.vulnweb.com/hpp/?pp=aa
          """)
    sys.exit(0)
    
get_url()    
    
    