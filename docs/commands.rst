Django-uWSGI management commands
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

runuwsgi
--------

.. code-block:: sh

   python manage.py runuwsgi

runuwsgi options:
-----------------

http
----
just 

.. code-block:: sh

   python manage.py runuwsgi http=8000


socket
------

.. code-block:: sh

   python manage.py runuwsgi socket=/tmp/projectname-uwsgi.sock

Other options
-------------

Any other options can be passed via environment variables, prefixed with UWSGI_