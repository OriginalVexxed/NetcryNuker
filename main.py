import sys
sys.dont_write_bytecode = True
import colorama
from colorama import Fore, init
from pystyle import Center, Write, Colors, Colorate
import os
import time
import subprocess

"""@a1lw and @loding_x coded this
if you are going to skid the code keep this please and thank you mr skid man"""

init()

options = """
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃   Discord: @a1lw and @loding_x  ┃     github.com/dropalways/     ┃
┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
┃                                 ┃  [8]                           ┃
┃  [1] Mass ban                   ┃  [9]                           ┃
┃  [2] Mass create channels       ┃  [10]                          ┃
┃  [3] Delete all channels        ┃  [11]                          ┃
┃  [4] Webhook spammer            ┃  [12]                          ┃
┃  [5] Discord nuker bot          ┃  [13]                          ┃
┃  [6]                            ┃  [14]                          ┃
┃  [7]                            ┃  [15]                          ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
"""

def banner():
    banner_text = """ ███▄    █ ▓█████▄▄▄█████▓ ▄████▄  ██▀███  ▓██   ██▓
 ██ ▀█   █ ▓█   ▀▓  ██▒ ▓▒▒██▀ ▀█ ▓██ ▒ ██▒ ▒██  ██▒
▓██  ▀█ ██▒▒███  ▒ ▓██░ ▒░▒▓█    ▄▓██ ░▄█ ▒  ▒██ ██░
▓██▒  ▐▌██▒▒▓█  ▄░ ▓██▓ ░ ▒▓▓▄ ▄██▒██▀▀█▄    ░ ▐██▓░
▒██░   ▓██░░▒████  ▒██▒ ░ ▒ ▓███▀ ░██▓ ▒██▒  ░ ██▒▓░
░ ▒░   ▒ ▒ ░░ ▒░   ▒ ░░   ░ ░▒ ▒  ░ ▒▓ ░▒▓░   ██▒▒▒ 
░ ░░   ░ ▒░ ░ ░      ░      ░  ▒    ░▒ ░ ▒░ ▓██ ░▒░ 
   ░   ░ ░    ░    ░ ░    ░          ░   ░  ▒ ▒ ░░  
         ░    ░           ░ ░        ░      ░ ░     """
    print(Colorate.Diagonal(Colors.red_to_purple, banner_text, 8))

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    os.system("title ball")
    banner()
    print(Colorate.Vertical(Colors.purple_to_red, options, 1))
    while True:
        user_input = Write.Input("\n\n━━trollinc""@netcry━>>> ", Colors.blue_to_red, interval=0.05)
        user_input = user_input.lower()
    
        if user_input == "1":
            subprocess.run(["python", "commands/massban.py"])
            time.sleep(1.9)
            main()
        elif user_input == "2":
            subprocess.run(["python", "commands/masschannel.py"])
            time.sleep(1.9)
            main()
        elif user_input == "3":
            subprocess.run(["python", "commands/massdelch.py"])
            time.sleep(1.9)
            main()
        elif user_input == "4":
            subprocess.run(["python", "commands/webhook.py"])
            time.sleep(1.9)
            main()
        elif user_input == "5":
            subprocess.run(["python", "commands/nuker.py"])
            time.sleep(1.9)
            main()
        else:
            print(Fore.RED +"Error 404 command not found")
            time.sleep(0.7)
            main()

if __name__ == "__main__":
    main()
