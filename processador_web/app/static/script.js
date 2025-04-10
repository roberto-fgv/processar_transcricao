document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('uploadForm');
    const textoProcessado = document.getElementById('textoProcessado');
    const downloadButton = document.getElementById('downloadButton');
    let textoProcessadoGlobal = '';
    const handleFormSubmit = (event) => {
        event.preventDefault();
        const mensagemErro = document.getElementById('mensagemErro');

        const formData = new FormData(form);

        fetch('/processar', {
            method: 'POST',
            body: formData
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Erro ao processar o arquivo.');
            }
            return response.json();
        })
        .then(data => {
            if (data.erro) {
                mensagemErro.textContent = data.erro;
                textoProcessado.value = '';
                downloadButton.style.display = 'none';
            } else {
                textoProcessadoGlobal = data.texto_processado;
                textoProcessado.value = data.texto_processado;
                mensagemErro.textContent = '';
                downloadButton.style.display = 'block';
            }
        })
        .catch(error => {
            mensagemErro.textContent = error.message;
            textoProcessado.value = '';
            downloadButton.style.display = 'none';
        });
    };

    const handleDownload = () => {
        const texto = textoProcessadoGlobal;

        const link = document.createElement('a');
        const file = new Blob([texto], { type: 'text/plain' });

        link.href = URL.createObjectURL(file);
        link.download = "transcricao_processada.txt";
        link.click();
        URL.revokeObjectURL(link.href);
    };

    form.addEventListener('submit', handleFormSubmit);
    downloadButton.addEventListener('click', handleDownload);

});
