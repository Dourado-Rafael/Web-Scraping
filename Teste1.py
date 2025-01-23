import os
import re
import requests
from bs4 import BeautifulSoup, SoupStrainer
from zipfile import ZipFile

url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

# Função para fazer o download do arquivo PDF
def download_pdf(pdf_url, filename):
    response = requests.get(pdf_url, stream=True)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192): 
                if chunk:  
                    f.write(chunk)

# Função para buscar os links dos PDFs no site
def get_pdf_links():
    response = requests.get(url)
    link_filter = SoupStrainer('a', href = re.compile(r'anexo.*\.pdf$', re.IGNORECASE))
    links = BeautifulSoup(response.text, 'html.parser', parse_only = link_filter)
    listas_link = []
    for link in links:
        listas_link.append(link.get('href'))
    return listas_link

# Função para compactar os PDFs em um arquivo ZIP
def compactar_em_zip(pdf_files, zip_filename):
    with ZipFile(zip_filename, 'w') as zipf:
        for pdf in pdf_files:
            zipf.write(pdf)
            print(f"Adicionando {pdf} ao arquivo ZIP.")
    print(f"Arquivos compactados em {zip_filename} com sucesso!")


pdf_links = get_pdf_links()

# Vamos considerar os dois primeiros links encontrados como sendo os anexos I e II
pdf_files = []
for i, link in enumerate(pdf_links, start=1):
    filename = f"Anexo_{i}.pdf"
    download_pdf(link, filename)
    pdf_files.append(filename)


compactar_em_zip(pdf_files, "Anexos.zip")

# Remover arquivos PDF individuais após compactação
for pdf in pdf_files:
    os.remove(pdf)
    print(f"Arquivo {pdf} removido após compactação.")
