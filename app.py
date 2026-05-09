#imports

from flask import Flask, render_template, request
import generateGraphs


app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if file:
        print('File uploaded successfully')
        return 'File uploaded successfully'

if __name__ == '__main__':
    app.run(debug=True)
