from os import abort
import os
from flask import Flask,request,render_template
from werkzeug.utils import secure_filename
from test import awesome
from multiprocessing import Process
app = Flask(__name__)

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/rahuldoneriya/Desktop/AudioSummariser/Code/Project.json"


class processClass:

    def __init__(self):
        p = Process(target=self.run, args=())
        p.daemon = True
        p.start()

    def run(self):
        l1=awesome()
        return l1


@app.route('/')
def upload_file():
    return render_template('/templates/profile.html')


@app.route('/content')
def content():
    text = open('btpsummary.txt', 'r+')
    context = text.read()
    text.close()
    return render_template('/templates/content.html', text=context)


@app.route('/processing', methods=['GET', 'POST'])
def upload_file1():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        try:
            begin = processClass()
        except:
            abort(500)

        return render_template('/templates/shit.html')
    else:
        return 'GeT'


def main():
    app.run(host='', threaded=True)


main()


if __name__ == '__main__':
    app.run(debug=True)
