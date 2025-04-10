from flask import render_template, jsonify, request, Response, make_response
from app import app
from app.forms import UploadForm 
from app.utils import processar_transcricao
import io

@app.route('/', methods=['GET', 'POST'])
def index():
    form = UploadForm()
    return render_template('index.html', form=form)

@app.route('/processar', methods=['POST'])
def processar():
    if 'arquivo' not in request.files:
        return jsonify({'erro': "Nenhum arquivo foi enviado"}), 400

    arquivo = request.files['arquivo']
    if arquivo.filename == '':
         return jsonify({'erro': "Nenhum arquivo foi enviado"}), 400
    
    
    try:
        try:
            texto = arquivo.read().decode('utf-8')
        except UnicodeDecodeError as e:
            print("Erro ao decodificar o arquivo:")
            print(str(e))            
            return jsonify({'erro': "Erro ao decodificar o arquivo. Certifique-se de que o arquivo esteja em formato UTF-8."}), 500
        texto_processado = processar_transcricao(texto)
        return jsonify({'texto_processado': texto_processado, 'sucesso': True})
    except Exception as e:        
        print("Erro ao processar o arquivo:")
        print(str(e))
        return jsonify({'erro': str(e)}), 500


@app.route('/download', methods=['GET'])
def download():
    try:
        texto_processado = request.args.get('text')
        if not texto_processado:
            return jsonify({'erro': "Nenhum texto fornecido para download"}), 400

        response = make_response(texto_processado)
        response.headers.set('Content-Disposition', 'attachment', filename='texto_processado.txt')
        response.headers.set('Content-Type', 'text/plain; charset=utf-8')
        return response
    except Exception as e:
        return jsonify({'erro': str(e)}), 500
