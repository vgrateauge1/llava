from flask import Flask, request, render_template,redirect, url_for,session,jsonify
from llava import *

import os

app = Flask(__name__)
app.secret_key = 'JaiPlusDeVoix'  # Définissez une clé secrète forte

llava = createLlava()
# Ensure there's a folder named 'uploads' in the same directory as this script
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/submit-text', methods=['POST'])
def handle_text():
    text = request.form['text']
    # Process the text as needed, e.g., save to a file or database
    print(text)  # For demonstration purposes

    return redirect(url_for('index'))  # Redirect back to the main page


@app.route('/', methods=['GET', 'POST'])
def index():
    message = ""
    if request.method == 'POST':
        # Assuming your input field's name is 'text'
        question = request.form['text']
        if 'uploaded_file_path' in session:
            file_path = session['uploaded_file_path']
            # Ici, vous pouvez associer `file_path` à `text` comme nécessaire
            # Par exemple, enregistrer dans une base de données ou un fichier
            question = f"{question} {file_path}"
            # Optionnel : Supprimer le chemin du fichier de la session après l'utilisation
            session.pop('uploaded_file_path', None)
        else:
            question = f"{question}"

        message = askLlava(llava,question)
        print(question,message)
        # You can process the message here if needed
    return render_template('index.html', message=message)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part', 400
    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400
    if file:
        filename = file.filename
        save_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(save_path)
        absolute_path = os.path.abspath(save_path)
        # Stocker le chemin du fichier dans la session
        session['uploaded_file_path'] = absolute_path
        return jsonify({'message': 'File uploaded successfully', 'path': absolute_path})
    else:
        return 'Upload failed', 500

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

if __name__ == '__main__':
    app.run(debug=True)
