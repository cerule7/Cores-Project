# Config values

import os
import pathlib

# The directory that the currently running code lives in (cores_web).
SOURCE_DIRECTORY = pathlib.Path(os.path.dirname(os.path.abspath(__file__)))

DATA_DIRECTORY = SOURCE_DIRECTORY / 'data'
# The path to the courses database. This will first check the environment to see if we've specified a file path, then
# will fall back to cores_web/data/courses.db. (This may make it easier to upload the app to a server environment
# later.)
COURSE_DATABASE_FILE = os.fspath(os.getenv('COURSE_DATABASE_FILE', DATA_DIRECTORY / 'courses.db'))

