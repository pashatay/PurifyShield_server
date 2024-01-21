from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from werkzeug.utils import secure_filename
from anonymizer import anonymize_file
import os

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "./uploads"
ALLOWED_EXTENSIONS = {"csv", "xlsx"}
CONFIG_FILE = "./anonymization_config.json"

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/upload", methods=["POST"])
def upload_file():
    try:
        if "file" not in request.files:
            return jsonify({"message": "No file part in the request"}), 400

        file = request.files["file"]

        if file.filename == "":
            return jsonify({"message": "No file selected for uploading"}), 400

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            input_file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            output_file_path = os.path.join(
                app.config["UPLOAD_FOLDER"], "anonymized_" + filename
            )
            config_path = os.path.join(CONFIG_FILE)

            file.save(input_file_path)

            anonymize_file(input_file_path, output_file_path, config_path)

            response = send_file(output_file_path, as_attachment=True)

            # Clean up: Remove uploaded and cleaned files
            os.remove(input_file_path)
            os.remove(output_file_path)

            return response
        else:
            return jsonify({"message": "Unsupported file format"}), 400
    except Exception as e:
        return jsonify({"message": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
