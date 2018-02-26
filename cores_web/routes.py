# All URL routes (logic that decides what shows up at what URL) are handled in this file.

from flask import render_template, request

from cores.core import Core
from cores_web import app, database

@app.route('/', methods=['GET', 'POST'])
def test_core_selection():
    if request.method == 'GET':
        # Display the available cores.
        return render_template('form.html', cores=sorted(Core, key=lambda core: core.code))
    elif request.method == 'POST':
        # Display the cores that the user has selected.
        #selected_cores = (Core(core_code) for core_code in request.form.keys() if bool(request.form.get(core_code)))
        return redirect(url_for("database"))
        #return '<br>'.join(core.code for core in selected_cores)


@app.route('/database', methods=['GET', 'POST'])

def the_database():
    #creates a set of cores from those selected 
    selected_cores = (Core(core_code) for core_code in request.form.keys() if bool(request.form.get(core_code)))
    coreset = yield_cores(selected_cores)
    missing_core = pick_core(coreset)
    return generate_descriptions(missing_core)[:3]

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
        return generate_descriptions("wc")
    if(not(search_core('QR', coreset))):
        return generate_descriptions("qr")
    if(not(search_core('QQ', coreset))):
        return generate_descriptions("qq")
    if(not(search_core('ITR', coreset))):
        return generate_descriptions("itr")
    if(not(search_core('NS', coreset))):
        return generate_descriptions("ns")
    if(not(search_core('NS2', coreset))):
        return generate_descriptions("ns")
    if(not(search_core('SCL', coreset))):
        return generate_descriptions("scl")
    if(not(search_core('WCd', coreset))):
        return generate_descriptions("wcd")
    if(not(search_core('WCr', coreset))):
        return generate_descriptions("wcr")
    if(not(search_core('HST', coreset))):
        return generate_descriptions("hst")
    if(not(search_core('CC', coreset))):
        return generate_descriptions("cc")
    if(not(search_core('CC2', coreset))):
        return generate_descriptions("cc")
    #only 2 Ahs are needed and these two are the most prevalent 
    if(not(check_ah(core))):
        if(not(search_core('AHp', coreset))):
            return generate_description("ahp")
        if(not(search_core('AHo', coreset))):
            return generate_description("aho")

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

import sys

def generate_descriptions(missing_core):
    core_courses = database.courses_with_core(missing_core)
    descriptions = (
        f'{course.number}: {course.name} ({", ".join(sorted(core.code for core in course.cores))})'
        for course in core_courses
    )
    return '<br>'.join(descriptions)


