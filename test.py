from flask import Flask
from flask import render_template, request

app = Flask(__name__)

core_codes = {"WC", "WCr", "WCd", "NS",
			  "NS 2", "SCL", "HST", "QQ",
			  "QR", "ITR", "CC", "CC 2",
			  "Ahp", "Ahq", "Aho", "Ahr"}


@app.route("/")
def form():
	return render_template('form.html')


@app.route("/", methods=["POST"])
def generate():
	cores = {core_code: bool(request.form.get(core_code)) for core_code in core_codes}
	return str(cores["WC"])

def process(coreslist):
	pass


if __name__ == "__main__":
	app.run()
