from colorama import Fore,Style,init
import socket
import os
import argparse
from banner import print_banner

init(autoreset=True)

class Banner:
    def __init__(self,host,port=80,timeout=2):
        self._host = host
        self._port = port
        self._timeout = timeout
        
    def grab_banner(self,reponseArray):
        try:
            bot = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            bot.settimeout(self._timeout)
            bot.connect((self._host,self._port))
            bot.send(b"HEAD / HTTP/1.0\r\n\r\n")
            decoded_response = b""
            while True:
                chunk = bot.recv(4096)
                if not chunk:
                    break
                decoded_response += chunk
            response = decoded_response.decode()
            print(f"{Fore.YELLOW}{response}")
            reponseArray.append(response) 
            bot.close()
        except Exception as e:
            print(f"{Fore.MAGENTA}Some error occured:{Fore.RED}{e}")

if __name__ == "__main__":
   
    print_banner()
   
    parser = argparse.ArgumentParser()
    
    parser.add_argument(
            "-t","--target",
            type=str,
            help="Enter the ip/web address of the target",
            required=True
            )
    
    parser.add_argument(
        "-p",
        "--port",
        type=int,
        help="Enter the port of the target on which to grab the banner",
        required=False,
        default=80
        )
    
    parser.add_argument("-w","--wait",
                        type=int,
                        help="Enter the default timeout value(in seconds)",
                        required=False,
                        default=2
                        )
    
    parser.add_argument(
        '-d','--directory',
        type=str,
        help="Enter the name of the directory where you want to store the result file",
        required=False,
        default = None
    )
   
    parser.add_argument(
        '-f','--filename',
        type=str,
        help="Enter the name of the file where to save the result",
        required = False,
        default = None
    )
    
    
    args = parser.parse_args()
    
    target = args.target
    port = args.port
    timeout = args.wait
    directory = args.directory
    filename = args.filename
    
    res = []

    print(Fore.CYAN + f"Grabbing banner of {target}:{port}")

    banner = Banner(target,port,timeout)
    banner.grab_banner(res)
    
    if directory != None and filename != None:
            os.makedirs(directory,exist_ok=True)
            with open(f"{directory}/{filename}",'w') as resultFile:
                resultFile.write(res[0])
    elif directory == None and filename != None:
        with open(filename,'w') as resultFile:
            resultFile.write(res[0])
    elif directory == None and filename == None:
        pass
    elif directory != None and filename == None:
        os.makedirs(directory,exist_ok=True)