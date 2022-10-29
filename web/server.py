import os
from flask import Flask, flash, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
from os.path import join, dirname, realpath
from II import readText

app = Flask(__name__,
            static_folder="static",
            template_folder='templates')

UPLOAD_FOLDER = join(dirname(realpath(__file__)), 'uploads')

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def static_file():
    return app.send_static_file("index.html")

def allowed_file(filename):     
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET','POST'])
def upload_file():

    def outData(word)->None:
        return """<p>{}</p> <style>p{{color:red;}}</style>""".format(word)


    if request.method == 'POST':
        if 'file' not in request.files:
            return 'there is no file in form!'
        file1 = request.files['file']
        path = os.path.join(app.config['UPLOAD_FOLDER'], file1.filename)
        file1.save(path)
        #print(path[path.index('web'):])
        

        pathNorm = path[path.index('web'):]

        res = readText(pathNorm)
        #print("res: ",res)
        words = []
        for _ in res:
            #print("_=",_)
            for i in _:
                if(isinstance(i, str)):
                    words.append(i)

        print("Нащ массив: ", words)

        out = ''
        for i in range(0, len(words)):
            out+=outData(words[i])

        return out
         
    else:
        return """<p>No such file, durak</p>"""



if __name__ == "__main__":
    app.run()