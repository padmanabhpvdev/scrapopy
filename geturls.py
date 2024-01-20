import requests
import os
import socket
from bs4 import BeautifulSoup
from urllib.parse import urljoin,urlparse
from rich.console import Console
from rich.table import Table

console = Console()

red='\033[0;31m'
nc='\033[00m'
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
def get_all_urls(url):
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "http://"+url
    try:
        print(f"Collecting all links from {url}")
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text,'html.parser')
            all_urls = set()
            for link in soup.find_all('a',href=True):
                absolute_url = urljoin(url,link['href'])
                all_urls.add(absolute_url)
            return all_urls
        else:
            print(f"{red}Error{nc}:Failed to retrieve the webpage. Status Code : {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        

def get_ip_address(hostname):
    try:
        ip_address = socket.gethostbyname(hostname)
        print(f"IP Address of {byellow}{hostname}{nc}: {yellow}{ip_address}{nc}")
    except socket.error as e:
        print(f"{red}Error{nc}:Unable to resolve {hostname} : {e}")
    
def get_details(ipaddr,url):
    try:
        response = requests.get(f"http://ip-api.com/json/{url}")
        if not url.startswith("http://") and not url.startswith("https://"):
            url = "http://"+url
        response_2 = requests.get(url)
        if response.status_code == 200:
            data = response.json()

            country = data.get('country')
            region = data.get('region','N/A')
            regionName = data.get('regionName','N/A')
            city = data.get('city','N/A')
            zip = data.get('zip','N/A')
            lat = data.get('lat','N/A')
            lon = data.get('lon','N/A')
            timezone = data.get('timezone','N/A')
            isp = data.get('isp','N/A')
            org = data.get('org','N/A')
            ass = data.get('as','N/A')
            query = data.get('query','N/A')

            report = f"Details of {url}:"
            print('\n'+report)
            print("-"*len(report)+'\n')
            tasks=[("Title",f"{response_2.text.split('<title>')[1].split('</title>')[0]}"),
            ("Status",f"{data['status']}"),
            ("Country",country),
            ("Region",region+' '+regionName),("City",city),
            ("ZipCode",zip),("Latitude",lat),("Longitude",lon),
            ("TimeZone",timezone),("ISP",isp),("Organization",org+' '+ass),
            ("Query",query)]
            table = Table(show_header=True,header_style="bold blue")
            table.add_column("Name")
            table.add_column("Description")
            for idx,task in enumerate(tasks,start=1):
                table.add_row(task[0],f"{task[1]}")
            console.print(table)
    except requests.RequestException as e:
        print(f"Error : {e}")

