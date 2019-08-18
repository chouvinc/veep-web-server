## This is a python server for VEEP.

## Table of Contents

[admin](#admin)

[dao](#dao)

[logic](#logic)

[main](#main)

[mappers](#mappers)

[static](#static)

[templates](#templates)

[util](#utils)

[others](#other)


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

## Heroku, Remote Host and Running Commands

Heroku is our hosting service, and has various commands that make it easy to debug and interact with prod
environment systems.

To run a command on a Heroku remote host, use `heroku run <command>`, where command is the command you
would run locally in terminal/bash, etc.

For example, locally one may want to run `flask shell` to work with imported values and ORM sqlalchemy.
Asking Heroku to do the same via `heroku run flask shell` will perform the same command but on our remote host.
This is good, since we can easily fix things unrelated to src code through local console!

app.config['key']

## For Bushi: A beginner's POV on differences between Flask & Django

I thought I'd include this section since I've worked with both frameworks; take this with a grain of salt
since I am also a beginner with Python web frameworks.

Some background: both frameworks are *full-stack integrated web development frameworks*.

**Full-stack** - traditional web-development (and, as you progress in your education, some other kinds of software development) 
designates a label to portions of any arbitrary application. 

"Front-end" generally means things that deal with the user;
eg. how a form interacts with a user's input, what clicks does a user need to make it to a certain page, what kind of
information the user needs to provide to do *something*.

"Back-end" is the "business" logic that deals with actually doing the thing. For example, if I were a customer for a website
that enables online transactions, the front-end would look like a credit-card information form. In comparison, the back-end would deal with tasks like verifying credit card information (with the corresponding bank), submitting a transaction 
request, and sending out a confirmation email.

Traditionally, these two types of development are treated as separate, and any pre-written software packages/libraries
isolate tasks of either type away from each other. Both Python and Flask *integrate* these two designations together.

**The differences** - my first impression of the two leads me to believe that Flask is more "lightweight" than Django. 
For any task that you want to do in either framework, Flask seems to require less initial setup. This comes at the 
cost of supplementing the provided functionality with your own custom-built logic. This has its own benefits -- mostly 
that you'll have to do less reading in general and you can get your app up and "running" quickly. I think this might be 
a bit of a bait though; most people (including me) don't really understand design considerations that the developers of
these frameworks have considered in building a scalable framework. Often times the additional documentation and reading
is annoying to go through at first, but after building out features and relatively extensive debugging, I've noticed that
it is in general more worth the time to read through framework documentation to use existing packages.

Anyways, this is getting long; just know that for any sort of large, non-script-type application, it is almost always
worth your time to spend more on reading, planning, and documenting, than it is to rush and crunch out code. Good luck!

PS: remember to leave what you've learned to newer cohorts of VEEP!

**Mappings of Django stuff to Flask:**

Flask (left) vs Django (right)

* `controllers.py` == `views.py`
* `sqlalchemy` == `models.py`
* `flash(<some_message>)` == `messages.<message_type>(<some_message)`
* package directory structure == `urls.py` -- basically Flask doesn't have the `urls.py` file structure like Django. It
uses the existing directory structure to determine url's.

##admin

Same as the Django admin portal, but much less. Flask requires us to dedicate a python package to represent url paths (recall 
that to define a url, we had to add a "path" object to urls.py via `path('www.somepath.com\<with_maybe_a_param>')`).

##dao

DAO is a term I yoinked from some enterprise Java development in my past internships. It stands for "Data Access Object"
and does exactly what it's named after: represent some database as an object in the language it's supported in (in this
case, Python). DAO files can work at any level -- as long as it returns a function or method that I can call to semantically 
do the same in the equivalent database language. If I want all "events", I should be able to call a function that does that
for me!

* `event_dao` - functions to interact with the `Events` table
* `member_dao` - functions to interact with the `Members` table
* `project_dao` - functions to interact with the `Projects` table
* `s3_dao` - functions to interact with AWS S3, a file-storage system that's optimized for space rather than runtime.

## logic

Once again, stuff from enterprise Java development design philosophies. The idea is that we isolate stuff that doesn't 
deal with UI/UX & other miscellaneous things that web development frameworks deal with (such as requests + status codes)
from the views (stored in the `main` package). Semantically, things like views should only be a controller for the visual representation of
things on your website. Included in that is resource retrieval; if I need to display some data, the view needs to make
a request for that data to whatever is storing it.

* `delete_logic` - functions to delete stuff (`Events`, `Members`, `Projects`)
* `edit_info_logic` - see above, but for edits (incomplete)
* `email_logic` - functions that send emails and handle our "Contact Us" page
* `get_objects_logic` - same as `delete_logic` and `edit_info_logic`, but only retrieves information
* `submit_info_logic` - same as above but writes information
* `web_logic` - specific version of `get_objects_logic`, generally for the purpose of displaying the data
on one of the pages

## main

Contains all of our views, which dictate what things the templates display. As mentioned before, in this
application, things that deal with _resources_ belong in `controllers.py`. Things that actually work with 
those resources -- eg. retrieve/update/delete/add them -- belong in `logic`.

## mappers

Miscellaneous files that provide simple mappings between objects. Useful for when the object structure returned by
`logic` or `dao` isn't easy to use through the template. Some examples:

If getting a Member object from the database returns a nested thing like this:

```json
{
  'id': 1,
  'member_name': 'Jimmy',
  {
    'year': 3,
    {
      'discipline': 'EngSci',
      'achievements': ['Drinks a lot of milk', '4.0 GPA', 'Full-ride Scholarship']
    }
  }
}
```

And I happen to need an object with at most 1 nested level, the mapper might do this:

```json
{
  'id': 1,
  'member_name': 'Jimmy',
  'year': 3,
  'discipline': 'EngSci',
  'achievements': ['Drinks a lot of milk', '4.0 GPA', 'Full-ride Scholarship']
}
```

Note that this example isn't in any way accurate, but serves to show why one might need a mapper.

## static

You already know this! Assets that remain the same regardless of what the user does remain in this package. Note, there
are some weird rules in Flask that deal with this that I can't remember. Read the official documentation and only the documentation;
tutorials online don't support different versions of Flask, and I remember specifically being stuck with a bug because of
unsupported versions.

# templates

Same as above.

## util

Usually random functionality that I couldn't find a package w/ a close enough semantic match to put it in. 

## misc

* `Pipfile/Pipfile.lock` - manages the different packages installed for the project, as well as their versions. 
Remember how every time someone added a package to the project and pushed to GitHub, you'd get `cannot find package <abc>`?
This solves that problem -- just run `pip install` every time before you run the project.
* `Procfile/Procfile.windows` - maps command names to the actual command for remote hosts (in this case Heroku).
* `test_basic` - this is our testing file (which I'm not very clear on how it works). A remnant of another VEEP
dev that kind of disappeared.