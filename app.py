from flask import Flask, request, render_template, jsonify
import pytesseract
from PIL import Image

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    # Check if an image was uploaded
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded!'}), 400
    
    # Read the uploaded image
    image = Image.open(request.files['image'])
    
    # Perform OCR using pytesseract
    text = pytesseract.image_to_string(image)
    
    return jsonify({'text': text})

@app.route('/', methods=['GET'])
def index():
    return render_template('page.html')

if __name__ == '__main__':
    app.run(debug=True)
