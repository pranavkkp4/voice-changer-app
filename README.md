# AI Voice Changer Web App

A Flask-based web application that lets users upload or record their voice and apply AI-style voice filters (deep, high-pitched, etc.) using pitch/speed changes.

## 🎯 Features
- 🎙️ Mic recording support
- 📁 Audio upload
- 🎚️ Voice presets (deep, medium, high for male/female)

## ⚙️ Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/yourusername/voice_changer_app.git
cd voice_changer_app
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Install FFmpeg:
- Windows: `choco install ffmpeg`
- macOS: `brew install ffmpeg`
- Linux: `sudo apt install ffmpeg`

4. Run the app:
```bash
python app.py
```

Then open [http://localhost:5000](http://localhost:5000) in your browser.

## 🌐 GitHub Deployment

To turn this into a GitHub repo:
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/yourusername/voice_changer_app.git
git push -u origin main
```

Be sure to create the repo on GitHub first and replace the URL with yours.

---
