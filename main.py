import os
import requests
import time
from bs4 import BeautifulSoup
from baixarItens import baixar_arquivo
from converterArquivos import converterZip

url = "https://dados-abertos-rf-cnpj.casadosdados.com.br/arquivos/2023-03-15/"  

response = requests.get(url)
pasta = "arquivos" + str(time.time())

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    
    empresa_links = []
    for link in soup.find_all('a', href=True):  
        if '.zip' in link['href'].lower():  
            empresa_links.append(link['href'])

    if not os.path.exists(pasta):
        os.makedirs(pasta)

    for link in empresa_links:
        baixar_arquivo( url+ link,link, pasta)

    
    converterZip(pasta)
else:
    print(f"Erro ao acessar o site. Código de status: {response.status_code}")



