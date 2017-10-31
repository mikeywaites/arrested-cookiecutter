==========================
Arrested Cookie Cutter
==========================

.. image:: https://badges.gitter.im/bruv-io/Arrested.png
    :target: https://gitter.im/bruv-io/Arrested

-------------------

This is a cookie-cutter for `Arrested https://github.com/mikeywaites/flask-arrested`_. - A Framework for rapidly building REST APIs with Flask.  This cookie-cutter creates a Flask application
that exposes a User API to help demonstrate how to use the different components of Arrested.


Installation
---------------------

If you haven't already installed Cookie Cutter then you'll need to do that first.

.. code-block: shell

    pip install cookiecutter

or read their documentation `here http://cookiecutter.readthedocs.io/en/latest/`_.


🚀 Get started in under a minute..
-----------------------------------------

Run the following commands to create a new project using the Arrested cookiecutter.

Step 1
^^^^^^^^^

Clone the project repo using cookiecutter (run cookiecutter --help for more options when creating the project)


.. code-block: shell

    cookiecutter gh:mikeywaites/arrested-cookiecutter -o arrested-users-api


Step 2
^^^^^^^^^^

Change to the newly created directory.

.. code-block: shell

    cd arrested-users-api

The directory should look something like this.

.. code-block: shell

    .
    └── arrested-users-api
        ├── Dockerfile
        ├── README.rst
        ├── arrested_users
        │   ├── __init__.py
        │   ├── apis
        │   │   ├── __init__.py
        │   │   └── v1
        │   │       ├── __init__.py
        │   │       ├── mappers
        │   │       │   ├── __init__.py
        │   │       │   ├── base.py
        │   │       │   └── user.py
        │   │       ├── middleware.py
        │   │       └── users.py
        │   ├── app.py
        │   ├── config.py
        │   ├── migrations
        │   │   ├── 266926b5775b_initial_migration.py
        │   │   └── script.py.mako
        │   ├── models
        │   │   ├── __init__.py
        │   │   ├── base.py
        │   │   └── user.py
        │   └── wsgi.py
        ├── arrested_users.db
        ├── docker-compose.yml
        ├── requirements.txt
        └── setup.py

    7 directories, 22 files

Step 3
^^^^^^^^^^

The example ships with a Docker container.  Read more about `Installing https://docs.docker.com/engine/installation/`-. and `Running https://docs.docker.com/get-started/ Docker`_.

.. code-block: shell

    docker-compose up api

Step 4
^^^^^^^^^^^^

Fire a HTTP request at the Users endpoint of your newly created API.

.. code-block: shell

    curl -u admin:secret localhost:8080/v1/users | python -m json.tool


The User Guide
--------------

Get started with Flask-Arrested using the quickstart user guide or take a look at the in-depth API documentation.

`<https://arrested.readthedocs.org>`_.

