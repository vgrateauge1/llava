from flask import Flask, request, jsonify, render_template, session, url_for, redirect
from werkzeug.utils import secure_filename
import logging
import os
import uuid
import llava

app = Flask(__name__)
app.secret_key = 'JaiPlusDeVoix'
app.config['UPLOAD_FOLDER'] = 'uploads'
logging.basicConfig(level=logging.DEBUG)

@app.route('/submit-text', methods=['POST'])
def handle_text():
    text = request.form['text']
    json_format = 'jsonFormat' in request.form
    
    logging.debug(f"Received text: {text}")
    if 'uploaded_file_path' in session:
        file_path = session['uploaded_file_path']
        logging.debug(f"Analyzing image at {file_path} with text: {text}")
        if json_format:
            jsonAnswer, llmanswer = llava.analyze_image(file_path, text)
            session.pop('uploaded_file_path', None)
            return render_template('index.html', message=jsonAnswer)  # Return JSON formatted response
        else:
            llmanswer = llava.analyze_criteria_image(file_path, text)
            session.pop('uploaded_file_path', None)
            return render_template('index.html', message=llmanswer)  # Return plain text response
    else:
        # Handle cases where there's no image uploaded but text is submitted
        message = "No image uploaded to analyze with text."
        return render_template('index.html', message=message)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', message="Upload an image and enter some text.")

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    filename = secure_filename(file.filename)
    file_id = str(uuid.uuid4())
    save_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(save_path)
    session['uploaded_file_path'] = save_path  # Store the file path in the session
    return jsonify({'message': 'File uploaded successfully', 'path': save_path, 'fileId': file_id})

@app.route('/delete-file', methods=['POST'])
def delete_file():
    file_id = request.form.get('id')
    if file_id:
        target_path = os.path.join(app.config['UPLOAD_FOLDER'], file_id)
        if os.path.exists(target_path):
            os.remove(target_path)
            return jsonify({'success': True})
        else:
            return jsonify({'success': False}), 404
    return jsonify({'success': False}), 400

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

if __name__ == '__main__':
    app.run(debug=True)
