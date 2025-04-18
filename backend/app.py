
from flask import Flask, request, jsonify
from pytube import YouTube
import os

app = Flask(__name__)

@app.route("/api/download", methods=["POST"])
def download():
    data = request.json
    url = data.get("url")
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        download_path = stream.download(output_path="downloads")
        return jsonify({"success": True, "download_url": "/downloads/" + os.path.basename(download_path)})
    except Exception as e:
        return jsonify({"success": False, "message": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
