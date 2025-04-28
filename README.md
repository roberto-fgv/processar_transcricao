# Web Transcription Processor

Este projeto é uma aplicação web que permite ao usuário fazer upload de arquivos de texto, processá-los para formatar timestamps e baixar o resultado formatado. A aplicação é construída em Flask (Python), HTML, CSS e JavaScript, oferecendo uma interface amigável para trabalhar com transcrições.

## Público-alvo e Objetivo

Esta aplicação foi desenvolvida principalmente para quem utiliza transcrições do YouTube para análise de dados. Ao copiar transcrições diretamente do YouTube, normalmente cada timestamp aparece em uma linha separada do texto, dificultando a análise e o processamento posterior. Esta ferramenta resolve esse problema ao colocar o timestamp e o texto correspondente na mesma linha, facilitando o uso dos dados em análises, planilhas e outras ferramentas.

### Exemplo de entrada (copiado do YouTube):
```
0:15 
Inicialmente, eu gostaria de entender quando
0:25 
e por que sua organização decidiu implementar as  metodologias ágeis nos processos de de auditoria?
```

### Saída após o processamento:
```
0:15 Inicialmente, eu gostaria de entender quando
0:25 e por que sua organização decidiu implementar as  metodologias ágeis nos processos de de auditoria?
```

## Estrutura do Projeto

```
processar_transcricao/
├── processador_web/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   ├── forms.py
│   │   ├── utils.py
│   │   ├── static/
│   │   │   ├── style.css
│   │   │   └── script.js
│   │   └── templates/
│   │       └── index.html
│   ├── run.py
│   ├── requirements.txt
│   └── README.md (documentação interna)
├── README.md (este arquivo principal)
└── ...
```

## Como Executar

1. **Pré-requisitos:**
   - Python 3.x
   - pip

2. **Instale as dependências:**
   - Abra o terminal e navegue até a pasta `processador_web`:
   ```sh
   cd processador_web
   pip install -r requirements.txt
   ```

3. **Execute a aplicação:**
   ```sh
   python run.py
   ```

4. **Acesse no navegador:**
   - Vá para `http://127.0.0.1:5000/`

## Como Usar

1. Selecione um arquivo `.txt` com a transcrição.
2. Clique em "Processar" para formatar os timestamps.
3. O texto processado será exibido na tela.
4. Clique em "Download" para baixar o arquivo formatado.

## Autor

Desenvolvido por [Roberto Rocha]
- 🌐 [Site Pessoal](https://roberto-rocha.tech)
- 🐙 [GitHub](https://github.com/roberto-fgv)
- 💼 [LinkedIn](https://www.linkedin.com/in/rsrocha/)
- 📧 E-mail: [rsantos.rocha@gmail.com](mailto:rsantos.rocha@gmail.com)
