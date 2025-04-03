# PDF to DOCX Converter

Este projeto é uma aplicação simples em Python que converte arquivos PDF para DOCX utilizando a biblioteca `pdf2docx`. A interface gráfica é construída com `tkinter`.

## Requisitos

Certifique-se de ter as seguintes bibliotecas instaladas antes de executar o script:

```sh
pip install pdf2docx tkinter
```

## Como Usar

1. Execute o script `python nome_do_arquivo.py`.
2. Clique no botão **"Browse PDF"** para selecionar um arquivo PDF.
3. Após selecionar o arquivo, clique em **"Convert to DOCX"** para iniciar a conversão.
4. O arquivo convertido será salvo no mesmo diretório com a extensão `.docx`.
5. Uma mensagem de sucesso será exibida ao final do processo.

## Estrutura do Código

- `select_pdf()`: Abre uma caixa de diálogo para selecionar um arquivo PDF.
- `convert_pdf()`: Converte o arquivo PDF para DOCX e exibe mensagens de erro ou sucesso.
- Interface gráfica com `tkinter`:
  - Entrada de texto para exibir o caminho do arquivo selecionado.
  - Botões para selecionar o arquivo e iniciar a conversão.

## Possíveis Melhorias

- Adicionar suporte para seleção do diretório de saída.
- Implementar barra de progresso para mostrar o andamento da conversão.
- Permitir conversão de múltiplos arquivos simultaneamente.

## Licença

Este projeto está sob a licença MIT.

