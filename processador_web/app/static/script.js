document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('uploadForm');
    const textoProcessado = document.getElementById('textoProcessado');
    const textoOriginal = document.getElementById('textoOriginal');
    const downloadButton = document.getElementById('downloadButton');
    let textoProcessadoGlobal = '';
    const handleFormSubmit = async (event) => {
        console.log('Formulário submetido!');
        event.preventDefault();
        const mensagemErro = document.getElementById('mensagemErro');

        const formData = new FormData(form);
        console.log(formData);

        fetch('/processar', {
            method: 'POST',
            body: formData            
        })
        .then(response => {
            const responseClone = response.clone();
            console.log('Response Clone:', responseClone);
            console.log('Response Clone OK:', responseClone.ok);
            if (!responseClone.ok) {
                console.log("erro in response.ok");                
                throw new Error('Erro ao processar o arquivo.');
            }       
            return responseClone.json();            

        })        
        .then(async data => {
            console.log("Data in then(data):", data);
            
           if (data.erro) {
                mensagemErro.textContent = data.erro;
                textoProcessado.value = '';
                downloadButton.style.display = 'none';
            } else {
                const fileInput = document.querySelector('input[type="file"]');
                const file = fileInput.files[0];
                console.log("file", file)
                console.log("file exists?", file != null)
                const fileText = await file.text();
                console.log("fileText", fileText);
                textoOriginal.value = fileText;
                

                textoProcessadoGlobal = data.texto_processado;
                textoProcessado.value = data.texto_processado;
                mensagemErro.textContent = '';
                downloadButton.style.display = 'block';
            }
        })
        .catch(error => {
            console.error('Erro:', error);
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
