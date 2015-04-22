Installation
============

django-uwsgi is easy installable via pip:

.. code-block:: sh

   pip install django-uwsgi


or clone it from `github <https://github.com/unbit/django-uwsgi>`_:


.. code-block:: sh

   git clone https://github.com/unbit/django-uwsgi.git
   cd django-uwsgi
   python setup.py install


By default ``django-uwsgi`` doesn’t installed with uWSGI as requirement.
And here are a few known reasons why:

* Django project installed into virtualenv and running in `Emperor <http://uwsgi-docs.readthedocs.org/en/latest/Emperor.html>`_ mode. In this case uWSGI is installed system-wide or into some other virtualenv.
* Some devs love to use system package managers like apt and prefer to install uwsgi other way.
* you need to build uWSGI with custom profile ex: ``UWSGI_PROFILE=gevent pip install uwsgi``

You can install django-uwsgi with uWSGI by appending [uwsgi] to the install command:

.. code-block:: sh

   pip install django-uwsgi[uwsgi]