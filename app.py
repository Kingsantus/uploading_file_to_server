import os 
from flask import request, jsonify, Flask
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'C:/Users/kingsantus/Documents/upload-file/static'

ALLOWED_EXTENSION = set(['pdf', 'docx', 'jpg', 'png', 'jpeg'])

def allowed_file(filename):
    """Validate a filename against the allowed extensions"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSION

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/media/upload', methods=['GET', 'POST'])
def upload_file():
    """ Upload a file to the server"""
    
    if 'file' not in request.files:
        return jsonify({'error': 'File not found'})
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'File not found'}), 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return jsonify({'success': 'File uploaded successfully'})

if __name__ == '__main__':
    app.run(debug=True)