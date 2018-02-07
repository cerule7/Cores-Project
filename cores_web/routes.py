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
        selected_cores = (Core(core_code) for core_code in request.form.keys() if bool(request.form.get(core_code)))
        return '<br>'.join(core.code for core in selected_cores)


@app.route('/database')
def test_database():
    # Display the number, name, and cores of every course that has the WCr core.
    wcr_courses = database.courses_with_core(Core.wcr)
    descriptions = (
        f'{course.number}: {course.name} ({", ".join(sorted(core.code for core in course.cores))})'
        for course in wcr_courses
    )
    return '<br>'.join(descriptions)
