# Chalice

My small blog and portfolio written in Python using Flask.

## Requirements
* Flask
* Flask-Login
* Flask-SQLAlchemy
* Pygments
* Markdown
* translitcodec

Easiest way to install these is via [easy_install](http://pypi.python.org/pypi/setuptools) or [pip](http://pypi.python.org/pypi/pip).

## Getting started

1. Rename `chalice/default_config.py` to `chalice/config.py`
2. Set your db connection string.
3. Set username and password for the admin interface.
4. Call `python createdb.py && python run.py`
5. Point your browser to [http:://localhost:5000/](http:://localhost:5000/)

## License
[BSD](http://opensource.org/licenses/BSD-2-Clause)