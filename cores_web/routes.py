# All URL routes (logic that decides what shows up at what URL) are handled in this file.

from flask import render_template, request
from cores.core import Core
from cores_web import app, database

app.secret_key = "super secret key"
global coreset
global chosen_courses
global suggested_courses

@app.route('/', methods=['GET', 'POST'])
def test_core_selection():
    if request.method == 'GET':
        # Display the available cores.
        return render_template('form.html', cores=sorted(Core, key=lambda core: core.code))
    elif request.method == 'POST':
        return redirect(url_for("database"))


@app.route('/database', methods=['GET', 'POST'])
def the_database():
	#creates a set of cores from those selected
	global coreset
	global chosen_courses
	global suggested_courses
	selected_cores = (Core(core_code) for core_code in request.form.keys() if bool(request.form.get(core_code)))
	coreset = yield_cores(selected_cores)
	if(complete_set(coreset)):
		return "Congrats, you've filled all of your requirements!"
	suggested_courses = pick_core(coreset)
	chosen_courses = []
	return render_template('suggested_courses_form.html', suggested_courses=suggested_courses, chosen_courses=chosen_courses)

def complete_set(coreset):
	size = len(coreset)
	if(search_core('AHo', coreset)):
		size -= 1
	if(search_core('AHp', coreset)):
		size -= 1
	if(search_core('AHr', coreset)):
		size -= 1
	if(search_core('AHq', coreset)):
		size -= 1
	return (check_ah(coreset) and size == 12)

def yield_cores(selected_cores):
	#Builds set of user's filled cores
	coreset = set()
	for c in selected_cores:
		coreset.add(c)
	return coreset


def search_core(str, coreset):
	#Return if a core is filled
	for c in coreset:
		if(c.code == str):
			return True
	return False


def pick_core(coreset):
    #Evaluates which missing core is rarest and returns classes with higest total cores
    #Expos must be filled first
    if(not(search_core('WC', coreset))):
        return query("wc", coreset)
    if(not(search_core('QR', coreset))):
        return query("qr", coreset)
    if(not(search_core('QQ', coreset))):
        return query("qq", coreset)
    if(not(search_core('WCd', coreset))):
        return query("wcd", coreset)
    if(not(search_core('WCr', coreset))):
        return query("wcr", coreset)
    if(not(search_core('ITR', coreset))):
        return query("itr", coreset)
    if(not(search_core('NS', coreset))):
        return query("ns", coreset)
    if(not(search_core('NS2', coreset))):
        return query("ns", coreset)
    if(not(search_core('SCL', coreset))):
        return query("scl", coreset)
    if(not(search_core('HST', coreset))):
        return query("hst", coreset)
    if(not(search_core('CC', coreset))):
        return query("cc", coreset)
    if(not(search_core('CC2', coreset))):
        return query("cc", coreset)
    #only 2 Ahs are needed and these two are the most prevalent
    if(not(check_ah(coreset))):
        if(not(search_core('AHp', coreset))):
            return query("ahp", coreset)
        if(not(search_core('AHo', coreset))):
            return query("aho", coreset)


def check_ah(coreset):
    #total Ahs filled
    sum = 0
    if(search_core('AHp', coreset)):
        sum += 1
    if(search_core('AHr', coreset)):
        sum += 1
    if(search_core('AHo', coreset)):
        sum += 1
    if(search_core('AHq', coreset)):
        sum += 1
    return (sum >= 2)


def cull_singles(core_courses, coreset):
	#removes inefficient courses that only fulfull a single core
	new_courses = [] 
	for course in core_courses:
		numcores = len(course.cores)
		for core in coreset:
			if core in course.cores:
				numcores -= 1
		if(len(course.cores) == 2 or numcores > 1 or len(coreset) > 14):
			new_courses.append(course)
	return new_courses[:6]


def query(missing_core, coreset):
	core_courses = database.courses_with_core(missing_core)
	if(missing_core != 'wc'):
		core_courses = cull_singles(core_courses, coreset)
	return core_courses

def get_description(course):
	return f'{course.number}: {course.name} ({", ".join(sorted(core.code for core in course.cores))})'

#def generate_descriptions(core_courses):
#	descriptions = (
#		f'{course.number}: {course.name} ({", ".join(sorted(core.code for core in course.cores))})'
#		for course in core_courses
#	)
#	return '<br>'.join(descriptions)

@app.route('/choices', methods=['GET', 'POST'])
def choices():
	global coreset
	global chosen_courses
	global suggested_courses
	suggested_courses = suggested_courses
	coreset = coreset
	chosen_courses = chosen_courses
	course = database.search_by_number(request.form["choice"])
	if course in chosen_courses:
		error = 'You have already chosen that course!'
		return render_template('suggested_courses_form.html', suggested_courses=suggested_courses, chosen_courses=chosen_courses, error=error)
	chosen_courses.append(course)
	print(course)
	for core in course.cores:
		coreset.add(core)
	suggested_courses = pick_core(coreset)
	return render_template('suggested_courses_form.html', suggested_courses=suggested_courses, chosen_courses=chosen_courses)
