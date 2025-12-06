import socket 
import threading 
from colorama import Fore,Style,init
import argparse
import os
from banner import print_banner

class ScanOpenPorts:
    def __init__(self,host,arr=None,timeout=2):
        self._host = host
        self._arr = arr if arr is not None else []
        self._timeout = timeout 
    
    def scan(self,port):
        try:
            bot = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            bot.settimeout(self._timeout)
            bot.connect((self._host,port))
            print(f"{Fore.GREEN}Port {Fore.YELLOW}{port} {Fore.MAGENTA}is open")
            self._arr.append(port)
            bot.close()
        except socket.error:
            print(f"{Fore.MAGENTA}Port {Fore.BLUE}{port} {Fore.MAGENTA}is close")
        except Exception as e:
            print(f"{Fore.RED}Some error occured:{e}")

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    
    parser.add_argument(
            "-t","--target",
            type=str,
            help="Enter the ip/web address of the target",
            required=True
            )
    
    parser.add_argument(
        "-i",
        "--initialRange",
        type=int,
        help="Enter the initial range of scannng port",
        required=True,
        default=1
        )
    
    parser.add_argument(
        "-f",
        "--finalRange",
        type=int,
        help="Enter the final range of scanning the ports",
        required=True,
        default=1000
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
        '-o','--open',
        type=str,
        help="Enter the name of the file where to save the result",
        required = False,
        default = None
    )
    
    print_banner()
    
    args = parser.parse_args()
    
    target = args.target
    initialRange = args.initialRange
    finalRange = args.finalRange
    timeout = args.wait
    directory = args.directory
    filename = args.open
    
    res = []

    scan = ScanOpenPorts(target,res,timeout)
    
    threads = []
    
    for i in range(initialRange,finalRange+1):
        thread = threading.Thread(target=scan.scan,args=(i,))
        thread.start()
        threads.append(thread)
        
    for thread in threads:
        thread.join()
        
    for port in res:
        print(port)
        
        if directory != None and filename != None:
            os.makedirs(directory,exist_ok=True)
            with open(f"{directory}/{filename}",'a') as resultFile:
                for port in res:
                    resultFile.write(str(port)+'\n')
        elif directory == None and filename != None:
            with open(filename,'a') as resultFile:
                for port in res:
                    resultFile.write(str(port)+'\n')
        elif directory == None and filename == None:
            pass
        elif directory != None and filename == None:
            os.makedirs(directory,exist_ok=True)