from flask import Flask, request, render_template, send_file
from werkzeug.utils import secure_filename
import os
from pydub import AudioSegment
from io import BytesIO

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def apply_preset(sound, preset):
    pitch = 1.0
    speed = 1.0

    presets = {
        'deep_male': (0.8, 1.0),
        'medium_male': (1.0, 1.0),
        'high_male': (1.2, 1.1),
        'deep_female': (1.1, 1.1),
        'medium_female': (1.3, 1.2),
        'high_female': (1.5, 1.3),
    }

    if preset in presets:
        pitch, speed = presets[preset]

    altered = sound._spawn(sound.raw_data, overrides={
        "frame_rate": int(sound.frame_rate * pitch)
    }).set_frame_rate(sound.frame_rate)

    altered = altered.set_frame_rate(int(altered.frame_rate * speed))
    altered = altered.set_frame_rate(sound.frame_rate)

    return altered

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_audio():
    if 'audio' not in request.files:
        return "No file uploaded", 400
    file = request.files['audio']
    preset = request.form.get('preset', 'medium_male')

    filename = secure_filename(file.filename)
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(filepath)

    sound = AudioSegment.from_file(filepath)
    processed = apply_preset(sound, preset)

    output = BytesIO()
    processed.export(output, format="wav")
    output.seek(0)

    return send_file(output, as_attachment=True, download_name="modified.wav", mimetype='audio/wav')

if __name__ == '__main__':
    app.run(debug=True)
