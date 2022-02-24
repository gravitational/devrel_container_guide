# to interact with the operarting system
import os

# import the Flask class from flask module
from flask import Flask
# importing the os module to interact with the operating system
import os

#instatiating the Flask class
app = Flask(__name__)


@app.route('/')
def route():
    return "hello world"

@app.route('/download')
def download_file():
    print("About to download the file....")
    # to execute wget command on the system and save the output in a file
    os.system('wget https://sample-videos.com/csv/Sample-Spreadsheet-10-rows.csv -O sample.csv')
    return "Done downloading the file."

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)