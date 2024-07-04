from flask import Flask, request, render_template, redirect, url_for
from ultralytics import YOLO
from PIL import Image
import os
from pyngrok import ngrok

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads/'
app.config['PREDICTED_FOLDER'] = 'static/predictions/'

# Create uploads and predictions directories if not exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['PREDICTED_FOLDER'], exist_ok=True)

# Load YOLO model
model = YOLO("runs/detect/train/weights/best.pt")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            
            # Make prediction
            image = Image.open(filepath)
            results = model.predict(source=image, conf=0.2, save=True)
            
            # Save the predicted image
            predicted_image_path = os.path.join(app.config['PREDICTED_FOLDER'], file.filename)
            results[0].save(predicted_image_path)
            
            return render_template('index.html', original=file.filename, prediction=file.filename)
    return render_template('index.html')

if __name__ == '__main__':
    # Start ngrok when the app runs
    public_url = ngrok.connect(5000)
    print(f" * Ngrok tunnel available at {public_url}")
    app.run()
