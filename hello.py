from flask import Flask
from flask import render_template,send_file
from pptx import Presentation
import io
from pptx.enum.shapes import MSO_SHAPE
from pptx.util import Inches
import Audio
app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('base.html')

@app.route('/startrecording/')
def hello():
    out_file = Audio.run_audio()
    return send_file(out_file, attachment_filename="testing.pptx", mimetype="application/vnd.openxmlformats-officedocument.presentationml.presentation", as_attachment=True,cache_timeout=0)
    #return render_template('base.html')

if __name__ == "__main__":
    app.run()   