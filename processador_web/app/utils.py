def processar_transcricao(texto):
    linhas = texto.splitlines()
    texto_processado = ""
    for linha in linhas:
        if "-->" in linha:
            texto_processado += f"<{linha}>\n"
        else:
            texto_processado += f"{linha}\n"
    return texto_processado
