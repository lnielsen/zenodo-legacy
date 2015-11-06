# -*- coding: utf-8 -*-
#
# This file is part of Zenodo.
# Copyright (C) 2015 CERN.
#
# Zenodo is free software; you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# Zenodo is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Zenodo; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston,
# MA 02111-1307, USA.
#
# In applying this license, CERN does not
# waive the privileges and immunities granted to it by virtue of its status
# as an Intergovernmental Organization or submit itself to any jurisdiction.


"""Module tests."""

from __future__ import absolute_import, print_function

from flask import Flask

from zenodo_legacy import ZenodoLegacy
from zenodo_legacy.views import blueprint


def test_version():
    """Test version import."""
    from zenodo_legacy import __version__
    assert __version__


def test_init():
    """Test extension initialization."""
    app = Flask('testapp')
    ext = ZenodoLegacy(app)
    assert 'zenodo-legacy' in app.extensions

    app = Flask('testapp')
    ext = ZenodoLegacy()
    assert 'zenodo-legacy' not in app.extensions
    ext.init_app(app)
    assert 'zenodo-legacy' in app.extensions


def test_blueprint_registration():
    """Test blueprint registration."""
    app = Flask('testapp')
    ZenodoLegacy(app)
    app.register_blueprint(blueprint)
