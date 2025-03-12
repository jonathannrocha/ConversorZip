import os
import requests

def baixar_arquivo( url, nomeArquivo, pasta ):
    
    caminho_atual = os.path.dirname(os.path.abspath(__file__))
    
    caminhoZip =  os.path.join( pasta, 'arquivosZips' )
    
    if not os.path.exists( caminhoZip):
        os.makedirs(caminhoZip)
  
    caminho_arquivo =  os.path.join(caminho_atual , caminhoZip, nomeArquivo  )
  
    response = requests.get(url, stream=True)
    
    if response.status_code == 200:
        with open(caminho_arquivo, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
            
            print(f'Arquivo criado com sucesso {caminho_arquivo}')


    