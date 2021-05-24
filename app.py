import os
import wget
import time
import requests


from flask import Flask, request, abort, jsonify, send_from_directory, redirect, url_for
from __init__ import renderize_voice

UPLOAD_DIRECTORY = "."

if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)

api = Flask(__name__)
api.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

def enviar_archivos_server(API_URL , filename):
    fin = open(filename, 'rb')
    files = {'file': fin}
    try:
        r = requests.post(API_URL, files=files)
        print (r.text)
    finally:
        fin.close()


@api.route("/voice" , methods=[ 'POST'])
def voice():
    content = request.json
    serial = content['out_name']
    print (content['lyrics'])
    print (content['midi'])
    print (content['sex'])
    print (content['tempo'])
    print (content['method'])
    print (content['language'])
    print (content['music'])
    renderize_voice(content['lyrics'],content['midi'],content['sex'],content['tempo'],'.',content['method'],content['language'],content['out_name'],content['music'])
    #enviar_archivos_server('http://127.0.0.1:8000/', 'voice.xml')
    #enviar_archivos_server('http://127.0.0.1:8000/', content['out_name']+'.wav')

    return jsonify({"voice":"voice_"+serial+".wav",
                   "song":"song_"+serial+".mp3",
                   "voicexml":"partitura_"+serial+".xml" })




   # enviar_archivos_server('http://127.0.0.1:8000/', 'voice.xml')
   # enviar_archivos_server('http://127.0.0.1:8000/', 'nicolasg.wav')
   # retu

@api.route("/files" , methods = [ 'GET'])
def list_files():
    """Endpoint to list files on the server."""
    files = []
    for filename in os.listdir(UPLOAD_DIRECTORY):
        path = os.path.join(UPLOAD_DIRECTORY, filename)
        if os.path.isfile(path):
            files.append(filename)
    return jsonify(files)


@api.route("/files/<path:path>")
def get_file(path):
    """Download a file."""
    return send_from_directory(UPLOAD_DIRECTORY, path, as_attachment=True)


@api.route("/files/<filename>", methods=["POST"])
def post_file(filename):
    """Upload a file."""
    if "/" in filename:
        # Return 400 BAD REQUEST
        abort(400, "no subdirectories allowed")

    with open(os.path.join(UPLOAD_DIRECTORY, filename), "wb") as fp:
        fp.write(request.data)

    # Return 201 CREATED
    return "", 201
                                                                                                                                  
UPLOAD_FOLDER = '.'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

api.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@api.route('/', methods=[ 'POST'])
def upload_file():
        file = request.files['file']
        print ('**found file', file.filename)
        #filename = secure_filename(file.filename)
        file.save(os.path.join(api.config['UPLOAD_FOLDER'], file.filename))
        # for browser, add 'redirect' function on top of 'url_for'
        return url_for('uploaded_file', filename=file.filename)

@api.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(api.config['UPLOAD_FOLDER'],filename)


if __name__ == "__main__":
    api.run(debug=True, port = 5070)

                                                                                                                                  
                                                                                                                                  

                                                                                                                                  
