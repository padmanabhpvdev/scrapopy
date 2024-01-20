import os
import geturls,requests
from rich.console import Console
from rich.table import Table

f = open("version.txt",'r')
response = requests.get("https://github.com/padmanabhpvdev//version.txt")
new_release = response.text
version = f.read()
console = Console()

black = "\033[0;30m"
red = "\033[0;31m"
bred = "\033[1;31m"
green = "\033[0;32m"
bgreen = "\033[1;32m"
yellow = "\033[0;33m"
byellow = "\033[1;33m"
blue = "\033[0;34m"
bblue = "\033[1;34m"
purple = "\033[0;35m"
bpurple = "\033[1;35m"
cyan = "\033[0;36m"
bcyan = "\033[1;36m"
white = "\033[0;37m"
nc = "\033[00m"

logo=f"""
{bred} (                                    )                  
{bred} )\ )                              ( /(                  
{bred}(()/(         (        )           )\())           (     
{red} /(_))   (    )(    ( /(   `  )   ((_)\    `  )    )\ )  
{red}(_))     )\  (()\   )(_))  /(/(     ((_)   /(/(   (()/(  
{byellow}/ __|   ((_)  ((_) ((_)_  ((_)_\   / _ \  ((_)_\   )(_)) 
{yellow}\__ \  / _|  | '_| / _` | | '_ \) | (_) | | '_ \) | || | 
{green}|___/  \__|  |_|   \__,_| | .__/   \___/  | .__/   \_, | 
{bgreen}                          |_|             |_|      |__/  
{nc} 
                   Version {version} 
                    
        Scrape Contents from a Webpage by Padmanabh PV                                                 
    """
commands = """
            [OPTIONS]

    [1] Get All URLs
    [2] Get details of a website
    [3] Get IP address of a website
    [4] Save All URLs in a txt file
    [5] Help
    [6] Exit
"""
print(logo)
if new_release > version:
    print(f"A newer version is available : {new_release}")
print(commands)
try:
    while True:
        command = input("ScrapOpy >>")
        if command == '1':
            url = input("Enter URL: ")
            all_url = geturls.get_all_urls(url)
            if all_url:
                print(f"Available URLs from {url}:")
                table = Table(show_header=True,header_style="bold blue")
                table.add_column("Index")
                table.add_column("Available Sublinks")
                for index,urls in enumerate(all_url):
                    table.add_row(f"{index+1}",urls)
                console.print(table)
        elif command == '2':
            url = input("Enter URL:")
            ip=geturls.get_ip_address(url)
            geturls.get_details(ip,url)
        elif command == '4':
            url = input("Enter URL: ")
            print("Collecting URLs...")
            all_url = geturls.get_all_urls(url)
            if all_url:
                print(f"Saving all URLs from {url}:")
                clean_url = url.replace("http://","").replace("https://","")#.replace(".","_")
                fname = f"data/{clean_url}.txt"
                if not os.path.exists("data"):
                    os.makedirs('data')
                with open(fname,'w')as f:
                    for urls in all_url:
                        f.write(urls + '\n')
                    print(f"{green}Success:{nc}File {yellow}{fname}{nc} saved successfully.")
        elif command == '3':
            url = input("Enter URL:")
            geturls.get_ip_address(url)
        elif command == '5':
            print(logo + '\n' +commands)
        elif command == '6' or command == 'exit':
            print('Stopping ScrapOpy...')
            exit()
        else:
            print("Invalid Option")
        
except KeyboardInterrupt:
    print("\nUser exiting using KeyboardInterrupt(Ctrl+C)")
