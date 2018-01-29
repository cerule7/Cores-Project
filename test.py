from flask import Flask
from flask import render_template, request
app = Flask(__name__)

@app.route("/")
def form():
    return render_template('form.html')

@app.route("/", methods=["POST"])
def generate():
	cores = {"WC": False, "WCr": False, "WCd": False, "NS": False, 
	"SCL": False, "HST": False, "QQ": False, "QR": False, "ITR": False,
	"CC": False, "Ahp": False, "Ahq": False, "Aho": False, "Ahr": False}
	if request.form.get("WC"):
		cores["WC"] = True
	if request.form.get("WCr"):
		cores["WCr"] = True
	if request.form.get("WCd"):
		cores["WCd"] = True
	if request.form.get("NS"):
		cores["NS"] = True
	if request.form.get("HST"):
		cores["HST"] = True
	if request.form.get("SCL"):
		cores["SCL"] = True
	if request.form.get("CC"):
		cores["CC"] = True
	if request.form.get("QQ"):
		cores["QQ"] = True
	if request.form.get("QR"):
		cores["QR"] = True
	if request.form.get("ITR"):
		cores["ITR"] = True
	if request.form.get("Ahp"):
		cores["Ahp"] = True
	if request.form.get("Aho"):
		cores["Aho"] = True
	if request.form.get("Ahr"):
		cores["Ahr"] = True
	if request.form.get("Ahq"):
		cores["Ahq"] = True

	return str(cores["WC"])

if __name__ == "__main__":
    app.run()


