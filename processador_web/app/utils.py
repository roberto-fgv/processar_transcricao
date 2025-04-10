import re

def processar_transcricao(texto):
    linhas = texto.split("\n")
    resultado = []
    timestamp = None

    for linha in linhas:
        match = re.match(r"(\d+:\d+)", linha)        
        if match:
            timestamp = match.group(1)
            if linha[len(timestamp):].strip():                
                resultado.append(f"{timestamp} {linha[len(timestamp):].strip()}")
            else:
                resultado.append(f"{timestamp} ")
                
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
