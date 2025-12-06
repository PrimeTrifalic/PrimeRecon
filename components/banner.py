import pyfiglet
from colorama import Fore,Style,init

init(autoreset=True)

def print_banner(text="Prime Trifalic"):
    print(pyfiglet.figlet_format(text, font="doom"))

if __name__ == "__main__":
    print_banner()