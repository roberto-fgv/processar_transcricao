import re
import tkinter as tk
from tkinter import filedialog, messagebox

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

def selecionar_arquivo():
    global input_file
    input_file = filedialog.askopenfilename(title="Selecione o arquivo de transcrição", filetypes=[("Arquivos de texto", "*.txt")])
    if input_file:
        status_label.config(text=f"Arquivo selecionado: {input_file}")
    else:
        status_label.config(text="Nenhum arquivo selecionado.")

def processar_arquivo():
    if not input_file:
        messagebox.showerror("Erro", "Por favor, selecione um arquivo primeiro.")
        return
    
    try:
        with open(input_file, "r", encoding="utf-8") as arquivo:
            texto_original = arquivo.read()
    except Exception as e:
         messagebox.showerror("Erro", f"Erro ao ler o arquivo: {e}")
         return
    
    texto_formatado = processar_transcricao(texto_original)
    texto_area.delete("1.0", tk.END)
    texto_area.insert(tk.END, texto_formatado)
    status_label.config(text="Arquivo processado. Clique em 'Salvar' para salvar o resultado.")
    
def salvar_arquivo():
    if texto_area.get("1.0", tk.END).strip() == "":
        messagebox.showerror("Erro", "Nenhum texto para salvar.")
        return

    output_file = filedialog.asksaveasfilename(title="Salvar arquivo formatado como", defaultextension=".txt", filetypes=[("Arquivos de texto", "*.txt")])
    if output_file:
        try:
            with open(output_file, "w", encoding="utf-8") as arquivo:
                arquivo.write(texto_area.get("1.0", tk.END))
            status_label.config(text=f"Texto formatado salvo em '{output_file}'.")
            messagebox.showinfo("Sucesso", f"Arquivo salvo com sucesso em '{output_file}'.")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao salvar o arquivo: {e}")

# Configuração da interface gráfica
root = tk.Tk()
root.title("Processador de Transcrição")

input_file = ""

label = tk.Label(root, text="Selecione o arquivo de transcrição:")
label.pack(pady=10)

selecionar_button = tk.Button(root, text="Selecionar Arquivo", command=selecionar_arquivo)
selecionar_button.pack(pady=5)

processar_button = tk.Button(root, text="Processar", command=processar_arquivo)
processar_button.pack(pady=5)

salvar_button = tk.Button(root, text="Salvar", command=salvar_arquivo)
salvar_button.pack(pady=5)

texto_area = tk.Text(root)
texto_area.pack(pady=10)

status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()