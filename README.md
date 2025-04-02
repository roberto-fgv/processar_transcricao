# Processador de Transcrição

Este script Python é utilizado para processar arquivos de transcrição de texto, formatando timestamps e organizando o conteúdo de forma mais legível.

## Funcionalidades

- Detecta timestamps no formato `minuto:segundo` (ex.: `0:15`, `1:00`) e os associa ao texto correspondente.
- Junta linhas de texto sem timestamp ao último timestamp detectado.
- Mantém linhas em branco para separação visual.
- Permite selecionar um arquivo de entrada e salvar o resultado processado em um arquivo de saída.

## Como usar

1. **Requisitos**:

   - Python 3.x instalado.
   - Biblioteca padrão `tkinter` (geralmente já incluída no Python).

2. **Execução**:

   - Execute o script no terminal ou em um ambiente Python.
   - Uma janela será aberta para selecionar o arquivo de transcrição de entrada (formato `.txt`).
   - Após o processamento, outra janela será aberta para salvar o arquivo formatado.

3. **Formato de Entrada**:

   - O arquivo de entrada deve conter timestamps no formato `minuto:segundo` no início das linhas, seguidos pelo texto correspondente.

4. **Formato de Saída**:
   - O arquivo de saída terá os timestamps organizados e o texto formatado.

## Exemplo de Entrada

```plaintext
0:15
Olá, bem-vindo à transcrição.
0:30
Este é um exemplo de como funciona. Aqui está uma linha sem timestamp.
```

## Exemplo de Saída

```plaintext
0:15
Olá, bem-vindo à transcrição.
0:30
Este é um exemplo de como funciona. Aqui está uma linha sem timestamp.
```

## Autor

Desenvolvido por [Roberto Rocha](https://roberto-rocha.tech).

- GitHub: [roberto-fgv](https://github.com/roberto-fgv)
- LinkedIn: [Roberto Rocha](https://www.linkedin.com/in/rsrocha/)
- E-mail: rsantos.rocha@gmail.com