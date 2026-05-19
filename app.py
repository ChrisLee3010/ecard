from flask import Flask, render_template, request
import qrcode
import io
import base64

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("form.html")

@app.route("/card")
def form():
    name = request.args.get("name", "")
    phone = request.args.get("phone", "")
    email = request.args.get("email", "")
    company = request.args.get("company", "")
    title = request.args.get("title", "")
    image_link = request.args.get("image_link", "")
    
    card_url = request.url
    
    qr = qrcode.make(card_url)
    buffer = io.BytesIO()
    qr.save(buffer, format="PNG")
    qr_base64 = base64.b64encode(buffer.getvalue()).decode()


    return render_template("card.html", name=name, phone=phone, email=email, company=company, title=title, image_link=image_link,qr_base64=qr_base64)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")