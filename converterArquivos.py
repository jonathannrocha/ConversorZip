import os
import requests
import zipfile

def converterZip( pasta ):
    caminho_atual = os.path.dirname(os.path.abspath(__file__))
    pastaFinal = os.path.join(pasta , 'csv' )

    if not os.path.exists(pastaFinal):
        os.makedirs(pastaFinal)

    pastaZips = os.path.join(caminho_atual , pasta, 'arquivosZips' )

    for item in os.listdir(pastaZips):
        caminho_item = os.path.join(pastaZips, item)

        try:
            with zipfile.ZipFile(caminho_item, 'r') as zip_ref:
                zip_ref.extractall(pastaFinal)
            
            print( f'item descompactado com sucesso { item }')
        except:
            print(f"Erro ao converter o {item} no path {caminho_item}")