import re
from tkinter import Tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

# Função para processar o texto
def processar_transcricao(texto):
    linhas = texto.split("\n")
    resultado = []
    timestamp = None

    for linha in linhas:
        # Detecta timestamps no formato "0:15", "1:00", etc.
        match = re.match(r"(\d+:\d+)", linha)
        if match:
            timestamp = match.group(1)
            resultado.append(f"{timestamp} {linha[len(timestamp):].strip()}")
        elif linha.strip():
            # Adiciona texto sem timestamp ao último timestamp
            if timestamp:
                resultado[-1] += f" {linha.strip()}"
            else:
                resultado.append(linha.strip())
        else:
            # Mantém linhas em branco para separação
            resultado.append("")

    return "\n".join(resultado)

# Abre uma janela para selecionar o arquivo de entrada
Tk().withdraw()  # Oculta a janela principal do Tkinter
input_file = askopenfilename(title="Selecione o arquivo de transcrição", filetypes=[("Arquivos de texto", "*.txt")])

if input_file:
    # Lê o texto do arquivo selecionado
    with open(input_file, "r", encoding="utf-8") as arquivo:
        texto_original = arquivo.read()

    # Processa o texto
    texto_formatado = processar_transcricao(texto_original)

    # Abre uma janela para salvar o arquivo de saída
    output_file = asksaveasfilename(title="Salvar arquivo formatado como", defaultextension=".txt", filetypes=[("Arquivos de texto", "*.txt")])

    if output_file:
        # Salva o resultado no arquivo selecionado
        with open(output_file, "w", encoding="utf-8") as arquivo:
            arquivo.write(texto_formatado)

        print(f"Texto formatado salvo em '{output_file}'.")
    else:
        print("Operação cancelada: arquivo de saída não selecionado.")
else:
    print("Operação cancelada: arquivo de entrada não selecionado.")