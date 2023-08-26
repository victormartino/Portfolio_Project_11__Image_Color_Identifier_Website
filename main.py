from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
from flask_bootstrap import Bootstrap
from image_handler import ImageHandler
from color_handler import ColorHandler
from PIL import Image
import os

UPLOAD_FOLDER = './static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")  # REPLACE WITH YOUR KEY
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
Bootstrap(app)


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('show_image', filename=filename))
        else:
            flash("Something went wrong. Please try again.")
    return render_template("index.html")


@app.route("/palette/<filename>")
def show_image(filename):
    uploaded_image = Image.open(UPLOAD_FOLDER + "/" + filename)
    image_analyzer = ImageHandler(uploaded_image)
    rgb_colors = image_analyzer.get_rgb_colors()
    hex_converter = ColorHandler(rgb_colors)
    hex_colors = hex_converter.get_hex_colors()
    return render_template('show-image.html', filename=filename, colors=hex_colors)


if __name__ == "__main__":
    app.run(debug=True)
