import sqlite3
from flask import g, Flask, current_app
from core_class import *

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

	##used to test 
	##search for all classes with a certain core 
	def main():
		cores_list = search_for_core("WCr")
		for i in cores_list:
			print(i.name)

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
		queryarg = core
		cores_list = []
		##find a way to fix this so there won't be SQL injections 
		##adds all classes with specified core to a list, order of total cores the class has
		##(most cores to least cores) 
		for courses in query_db('select * from courses where ' + core + ' = "1" ORDER BY total'):
			dict = create_cores_dict(courses[1])
			i = CoreClass(courses[1], courses[0], dict);
			cores_list.insert(0, i)
		return cores_list

	main()



