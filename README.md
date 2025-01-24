# Projeto de Download e Compactação de PDFs

Este projeto realiza o download de arquivos PDF a partir de um site, os compacta em um único arquivo ZIP e, em seguida, remove os arquivos PDF individuais.

## Descrição

O código faz o scraping de um site governamental para buscar links para arquivos PDF, realiza o download desses PDFs, compacta-os em um arquivo ZIP e finalmente exclui os arquivos PDF originais para liberar espaço. O script utiliza as bibliotecas `requests`, `BeautifulSoup` e `ZipFile` para automatizar o processo.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação
- **requests**: Para fazer requisições HTTP e baixar os PDFs
- **BeautifulSoup**: Para fazer o scraping da página HTML e buscar links para os PDFs
- **ZipFile**: Para compactar os PDFs em um arquivo ZIP
- **re**: Para aplicar expressões regulares e filtrar os links

## Requisitos

- Python 3.x
- Bibliotecas Python:
    - `requests`
    - `beautifulsoup4`
    - `re` (inclusa no Python)
    - `zipfile` (inclusa no Python)

## Instalação

1. Clone o repositório:

    ```bash
    git clone https://github.com/seu-usuario/nome-do-repositorio.git
    cd nome-do-repositorio
    ```

2. Instale as dependências necessárias:

    ```bash
    pip install requests beautifulsoup4
    ```

## Uso

1. Execute o script Python:

    ```bash
    python baixar_e_compactar_pdfs.py
    ```

2. O script realizará as seguintes etapas:
   - Buscará os links para os arquivos PDF no site especificado.
   - Baixará os dois primeiros arquivos PDF encontrados e os salvará como `Anexo_1.pdf` e `Anexo_2.pdf`.
   - Compactará os arquivos PDF em um único arquivo ZIP chamado `Anexos.zip`.
   - Excluirá os arquivos PDF individuais após a compactação.


