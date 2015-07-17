# Copyright 2015 Jason Heeris, jason.heeris@gmail.com
# 
# This file is part of the dungeon excavator web interface ("webcavate").
#
# Webcavate is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# Webcavate is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# webcavate. If not, see <http://www.gnu.org/licenses/>.

# Debugging is on.
DEBUG = True

# Define the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))  

# Define the database - we are working with
# SQLite for this example
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
DATABASE_CONNECT_OPTIONS = {}

# Session lifetime in seconds.
PERMANENT_SESSION_LIFETIME = 300

# Number of application threads.
THREADS_PER_PAGE = 1

# General security and secret stuff.
CSRF_ENABLED     = True
CSRF_SESSION_KEY = b'\xc4\xd9\xfc\x1d\xda\xd5\xab\x0cYG\xb9\xf7G\xa0\x1a\x98\x8c\t\xa7\xc4Y|\x07_'
SECRET_KEY       = b'2_\xe1\x80k\x940\x04\x19\xda\xfd/\xa5\xf9E\xe4D\xd3i\x1f\xd1\x84;\n'
