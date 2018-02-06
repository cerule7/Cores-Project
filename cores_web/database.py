# All database interactions should be handled in this file.

import re
import sqlite3

from cores.core import Core
from cores.course import Course
from cores_web import app


with app.app_context():
    _course_database = sqlite3.connect(app.config['COURSE_DATABASE_FILE'])


# Close the course database when the app shuts down.
@app.teardown_appcontext
def close_course_database(exception):
    _course_database.close()


def _query_db(query):
    cursor = _course_database.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    return rows


# Regex used to find all core codes in a string.
_core_pattern = re.compile('|'.join(reversed(sorted(core.code for core in Core))))


def _parse_course_codes(string):
    """
    Parses out the core codes from a database string using regex; avoids the need to query the database multiple times
    to figure out what cores a course fulfills.
    """
    return _core_pattern.findall(string)


def courses_with_core(core):
    # There's no risk of SQL injection because we're not using user-submitted course strings; this function only
    # accepts objects of our own Core class.
    for row in _query_db(f'select * from courses where {core.code} = "1" ORDER BY total'):
        name = row[1]
        number = row[0]
        cores = set(map(Core, _parse_course_codes(row[3])))
        yield Course(name, number, cores)
