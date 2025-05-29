from flask import (
    Flask, render_template, request, send_file, abort, after_this_request
)
from utils import change_frequency
from werkzeug.utils import secure_filename
import tempfile
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    try:
        if 'file' not in request.files:
            return 'No file part'

        file = request.files['file']
        if file.filename == '':
            return 'No selected file'

        hz_option = request.form.get('hz_option')
        if hz_option is None or not hz_option.isdigit():
            return 'Please enter a valid Hz value (e.g., 444, 1111)'

        target_hz = int(hz_option)
        if not (20 <= target_hz <= 20000):
            return 'Please enter a valid Hz value between 20 and 20000'

        filename = secure_filename(file.filename)

        # Save uploaded file to a temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_file:
            file.save(temp_file.name)
            temp_file_path = temp_file.name

        # Change frequency and get path to modified WAV
        modified_file_path = change_frequency(temp_file_path, target_hz)

        # Clean up temp files after response is sent
        @after_this_request
        def cleanup(response):
            try:
                os.remove(temp_file_path)
                os.remove(modified_file_path)
            except Exception as e:
                app.logger.warning(f"Cleanup failed: {e}")
            return response

        # New filename for download
        new_filename = f"{target_hz}Hz_{filename.replace('.mp3', '.wav')}"

        return send_file(modified_file_path, as_attachment=True, download_name=new_filename)

    except Exception as e:
        app.logger.error(str(e))
        abort(500, description='An unexpected error occurred')

if __name__ == '__main__':
    app.run(debug=True)
    