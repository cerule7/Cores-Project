class CoreClass:
	name = ""
	number = ""
	cores = {"WC": False, "WCr": False, "WCd": False, 
	"NS": False, "SCL": False, "HST": False, "QQ": False, 
	"QR": False, "ITR": False,"CC": False, "Ahp": False, 
	"Ahq": False, "Aho": False, "Ahr": False}

	def __init__(self, name, number, cores):
		self.name = name
		self.number = number
		self.cores = cores