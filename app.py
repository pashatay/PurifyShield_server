from flask import Flask, request, jsonify, send_file
from flask_cors import CORS  # Import CORS
from werkzeug.utils import secure_filename
from anonymizer import anonymize_file
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

UPLOAD_FOLDER = "./uploads"
ALLOWED_EXTENSIONS = {'csv', 'xlsx'}
CONFIG_FILE = "./anonymization_config.json"

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
        config_path = os.path.join(CONFIG_FILE)  # Path to the config file

        file.save(input_file_path)

        try:
            anonymized_file_path = anonymize_file(input_file_path, output_file_path, config_path)
            return send_file(anonymized_file_path, as_attachment=True)
        except Exception as e:
            return jsonify({'message': str(e)}), 500
    else:
        return jsonify({'message': 'Unsupported file format'}), 400

if __name__ == '__main__':
    app.run(debug=True)