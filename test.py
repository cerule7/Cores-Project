from flask import Flask
from flask import render_template, request
from database import *

app = Flask(__name__)

core_codes = {"WC", "WCr", "WCd", "NS",
			  "NS 2", "SCL", "HST", "QQ",
			  "QR", "ITR", "CC", "CC 2",
			  "Ahp", "Ahq", "Aho", "Ahr"}


@app.route("/")
##renders website 
def form():
	return render_template('/website.html')

#posts checkbox results to server
##creates dictionary of user's completed cores 
@app.route("/", methods=["POST"])
def generate():
	cores = {core_code: bool(request.form.get(core_code)) for core_code in core_codes}
	return database.fill(cores)

if __name__ == "__main__":
	app.run()
