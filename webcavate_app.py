#!/usr/bin/env python
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
import argparse

from flask import Flask, session

from webcavate.blueprint import webcavate_bp

HELP_TEXT = """\
Web interface to the dungeon excavator."""

# The WSGI thingo.
app = Flask(__name__)

# The configuration.
app.config.from_object('config')

# The webcavate module.
app.register_blueprint(webcavate_bp)

def main():
    """ Parse arguments and get things going for the web interface """
    parser = argparse.ArgumentParser(description=HELP_TEXT)
    
    parser.add_argument(
        '-p', '--port',
        help="Port to serve the interface on.",
        type=int,
        default=5050
    )

    parser.add_argument(
        '-a', '--host',
        help="Host to server the interface on.",
    )

    args = parser.parse_args()

    app.run(port=args.port, host=args.host, debug=True)

if __name__ == '__main__':
    main()
