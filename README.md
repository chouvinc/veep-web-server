##This is a python server for VEEP.

##Table of Contents (to be updated)

## Starting a Development Server

You will need to install the following:
* pipenv (dependency manager + virtualenv) - https://pipenv.readthedocs.io/en/latest/
* virtualenvwrapper (wrapper utility around virtualenv) - https://virtualenvwrapper.readthedocs.io/en/latest/

Pipenv is a dependency manager, similar to NPM, and writes to a file called a Pipfile. The Pipfile tracks
any external packages you may have added to your project when you use its equivalent command to `pip install`,
`pipenv install`. Pipenv will also only write to your current virtual environment, meaning that if 
one dependency breaks another, you can easily delete that virtual environment and start over (as opposed
to manually going through your hard drive/SSD and deleting python modules).

Virtualenvwrapper is a set of extensions that help you create, update, delete virtualenv's. It's not essential,
but I don't know how to do it conventionally with just virtualenv. It looks like you can actually create a
virutalenv with pipenv as well, though the tutorial I went through just used virtualenvwrapper.

To start a development server:
* make a new virtualenv
* run `pipenv run python setup.py`
* go to localhost:5000

app.config['key']