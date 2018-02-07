import sqlite3
from flask import g, Flask, current_app
from CoreClass import *

app = Flask(__name__)

with app.app_context():
	##change this to the location of your database file
	DATABASE = 'C:\\Users\\Charlie\\cores\\courses.db'

	##connects to database
	def get_db():
	    db = getattr(g, '_database', None)
	    if db is None:
	        db = g._database = sqlite3.connect(DATABASE)
	    return db

	##pass a string sql statement to query the database
	def query_db(query, args=(), one=False):
	    cur = get_db().execute(query, args)
	    rv = cur.fetchall()
	    cur.close()
	    return (rv[0] if rv else None) if one else rv

	@app.teardown_appcontext
	def close_connection(exception):
	    db = getattr(g, '_database', None)
	    if db is not None:
	        db.close()

	##returns a dictionary of all cores for a specific class
	def create_cores_dict(classname):
		core_codes = {"WC" : False, "WCr" : False, "WCd" : False, "NS" : False,
			  "SCL" : False, "HST" : False, "QQ" : False,
			  "QR" : False, "ITR" : False, "CC" : False,
			  "Ahp" : False, "Ahq" : False, "Aho" : False, "Ahr" : False}
		for key in core_codes: 
			i = query_db('select (" +key+ ") from courses where name = (" +classname+ ")')
			if(i == 1): 
				core_codes(key, True)
		return core_codes

	def search_for_core(core):
		cores_list = []
		##adds all classes with specified core to a list, order of total cores the class has
		##(most cores to least cores) 
		for courses in query_db('select * from courses where ' + core + ' = "1" ORDER BY total'):
			dict = create_cores_dict(courses[1])
			i = CoreClass(courses[1], courses[0], dict);
			cores_list.insert(0, i)
		return cores_list

	def check_ah(dict):
		sum = 0;
		if(dict("Ahp") == True):
			sum = sum + 1
		if(dict("Aho") == True):
			sum = sum + 1		
		if(dict("Ahq") == True):
			sum = sum + 1
		if(dict("Ahr") == True):
			sum = sum + 1
		return sum

	##finds the rarest unfilled core,  returns top 3 classes with the most cores 
	def fill(user_dict):
		##expos must always be filled first 
		if(user_dict.get("WC") == False):
			exposdict = {"WC" : True, "WCr" : False, "WCd" : False, "NS" : False,
			  "SCL" : False, "HST" : False, "QQ" : False,
			  "QR" : False, "ITR" : False, "CC" : False,
			  "Ahp" : False, "Ahq" : False, "Aho" : False, "Ahr" : False}
			c = [CoreClass("Expository Writing", "01:355:101", exposdict)]
			return c
		if(user_dict.get("QR") == False):
			return search_for_core("QR")[0:3]
		if(user_dict.get("QQ") == False):
			return search_for_core("QQ")[0:3]
		if(user_dict.get("ITR") == False):
			return search_for_core("ITR")[0:3]
		if(user_dict.get("NS") == False):
			return search_for_core("NS")[0:3]
		if(user_dict.get("NS 2") == False):
			return search_for_core("NS")[0:3]
		if(user_dict.get("SCL") == False):
			return search_for_core("SCL")[0:3]
		if(user_dict.get("WCd") == False):
			return search_for_core("WCd")[0:3]
		if(user_dict.get("WCr") == False):
			return search_for_core("WCr")[0:3]
		if(user_dict.get("HST") == False):
			return search_for_core("HST")[0:3]
		if(user_dict.get("CC") == False):
			return search_for_core("CC")[0:3]
		if(user_dict.get("CC 2") == False):
			return search_for_core("CC")[0:3]
		##you only need two different Ahs 
		if(check_ah(user_dict) < 2):
			if(user_dict.get("Ahr") == True):
				return ((search_for_core("Ahp") + search_for_core("Aho") + search_for_core("Ahq")))[0:6]
			if(user_dict.get("Aho") == True):
				return ((search_for_core("Ahp") + search_for_core("Ahr") + search_for_core("Ahq")))[0:6]
			if(user_dict.get("Ahp") == True):
				return ((search_for_core("Ahr") + search_for_core("Aho") + search_for_core("Ahq")))[0:6]
			if(user_dict.get("Ahq") == True):
				return ((search_for_core("Ahp") + search_for_core("Aho") + search_for_core("Ahr")))[0:6]

	##used to test 
	##search for all classes with a certain core 
	def main():
		core_codes = {"WC" : True, "WCr" : False, "WCd" : False, "NS" : False,
			  "SCL" : False, "HST" : False, "QQ" : False,
			  "QR" : False, "ITR" : False, "CC" : False,
			  "Ahp" : False, "Ahq" : False, "Aho" : False, "Ahr" : False}
		cores_list = fill(core_codes)
		if(len(cores_list) == 1):
			print (cores_list.name)
		else:
			for i in cores_list:
				print (i.name)

	##main()



