from bs4 import BeautifulSoup  
import requests

x = requests.get('https://es.motorsport.com/f1/drivers/')
soup = BeautifulSoup(x.text, 'html.parser')
lista_de_pilotos=(soup.find_all("p", {"class": "ms-item__title msf-primary-2xl-semibold"}))
for i in range(len(lista_de_pilotos)):
    lista_de_pilotos[i]=lista_de_pilotos[i].text[13:-8].replace("é","e")  
wiki_links=[]
f1_links=[]
ms_links=[]
for i in lista_de_pilotos:
    wiki_links.append(i.replace(" ","_"))
    f1_links.append(i.replace(" ","-").lower())
    ms_links.append(i.replace(" ","-").lower())

url_wiki="https://es.wikipedia.org/wiki/"
url_f1="https://www.formula1.com/en/drivers/"
url_ms="https://es.motorsport.com/driver/"

pilotos={}

for i in range(len(lista_de_pilotos)):
    pilotos[lista_de_pilotos[i]]=[]
    #wiki
    link=url_wiki+wiki_links[i]
    x = requests.get(link)
    soup = BeautifulSoup(x.text, 'html.parser')
    pilotos[lista_de_pilotos[i]].append(soup)
    #f1
    link=url_f1+f1_links[i]
    x = requests.get(link)
    soup = BeautifulSoup(x.text, 'html.parser')
    pilotos[lista_de_pilotos[i]].append(soup)
    #ms
    link=url_ms+ms_links[i]
    x = requests.get(link)
    soup = BeautifulSoup(x.text, 'html.parser')
    pilotos[lista_de_pilotos[i]].append(soup)
