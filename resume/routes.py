import os
import secrets

from flask import (
    current_app as app,
    render_template,
    jsonify,
    json,
    request,
    send_from_directory,
    url_for,
)
from weasyprint import HTML

DIRECTORY = app.config.get("PDF_PATH")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
    data = json.loads(request.data)
    html = render_template("resumes/1.html", data=data)
    filename = secrets.token_hex(10) + ".pdf"
    pdf = HTML(string=html).write_pdf(os.path.join(DIRECTORY, filename))

    return jsonify({"url": url_for("send_pdf", name=filename, _external=True)})


@app.route("/pdf/<name>")
def send_pdf(name):
    return send_from_directory(DIRECTORY, name)
