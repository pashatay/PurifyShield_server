from flask import Flask, request, jsonify, send_file
from werkzeug.utils import secure_filename
from anonymizer import anonymize_file
import os

app = Flask(__name__)

UPLOAD_FOLDER = "./uploads"
ALLOWED_EXTENSIONS = {'csv', 'xlsx'}

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['POST'])
def upload_file():
    
    if 'file' not in request.files:
        return jsonify({'message': 'No file part in the request'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'message': 'No file selected for uploading'}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        input_file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        output_file_path = os.path.join(app.config['UPLOAD_FOLDER'], "anonymized_" + filename)
        file.save(input_file_path)
        
        anonymized_file_path = anonymize_file(input_file_path, output_file_path)
        return send_file(anonymized_file_path, as_attachment=True)
    else:
        return jsonify({'message': 'Unsupported file format'}), 400

if __name__ == '__main__':
    app.run(debug=True)