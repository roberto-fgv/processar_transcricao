# Web Transcription Processor

This project is a web application that allows users to upload text files, process them to format timestamps, and then download the formatted output. The application is built using Flask (a Python web framework), HTML, CSS, and JavaScript, and it provides a user-friendly interface for working with transcriptions.

## Project Structure

The project is organized into the following directory structure:

```
processador_web/
├── app/                     # Main application code
│   ├── __init__.py          # Flask app initialization
│   ├── routes.py            # API routes and request handling
│   ├── forms.py             # Form definitions (e.g., upload form)
│   ├── utils.py             # Utility functions (e.g., text processing)
│   ├── static/              # Static files (CSS, JavaScript)
│   │   ├── style.css        # CSS styles
│   │   └── script.js        # JavaScript for client-side logic
│   └── templates/           # HTML templates
│       └── index.html       # Main web page
├── run.py                   # Script to run the Flask application
├── requirements.txt         # Project dependencies
└── README.md                # Project documentation
```

## How to Run

Before running the project, make sure you have Python and pip installed on your system. Then, follow these steps:

1.  **Install Dependencies:**
    *   Navigate to the `processador_web` directory in your terminal.
    *   Run the following command to install the project dependencies:

        ```bash pip install -r requirements.txt```

2.  **Run the Application:**
    *   Still in the `processador_web` directory, execute the `run.py` script:
    
        ```bash python run.py```

3.  **Access the Application:**
    *   Open your web browser.
    *   Go to `http://127.0.0.1:5000/`.

## How to Use

1.  **Select a File to Process:**
    *   On the web page, use the file input to select a `.txt` file containing the transcription you want to process.

2.  **Process the File:**
    *   Click the "Processar" button.
    *   The application will process the transcription, format the timestamps, and display the results in the text area on the page. The page will not be reloaded.

3.  **Download the Processed File:**
    *   Once the text is processed, a "Download" button will appear.
    *   Click the "Download" button to save the formatted text to a file on your computer.

## Autor

Desenvolvido por [Roberto Rocha].

- 🌐 [Site Pessoal](https://roberto-rocha.tech)
- 🐙 [GitHub](https://github.com/roberto-fgv)
- 💼 [LinkedIn](https://www.linkedin.com/in/rsrocha/)
- 📧 E-mail: [rsantos.rocha@gmail.com](mailto:rsantos.rocha@gmail.com)
