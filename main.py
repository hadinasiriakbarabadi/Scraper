from this import s
from bs4 import BeautifulSoup
import os
import functions
import requests

def main_scraper(url,directory):
    functions.create_directory(directory)
    source_code=requests.get(url)
    source_text=source_code.text
    soup=BeautifulSoup(source_text,"html.parser")
    print(source_text)

main_scraper("https://www.digikala.com","Calmancode")




