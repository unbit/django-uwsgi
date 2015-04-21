Things Todo for Django-uWSGI
~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Tests
* Create ``stats.py`` and and use it to get uWSGI stats in ``views.py`` and ``panels.py`` or by some other application(more DRY)
* Add to repo email & cache backends, runuwsgi, CBV mixins
* uWSGI config generator
* `Docs <http://django-uwsgi.readthedocs.org/en/latest/>`_
* Translations?
* Screenshots
* Add Django models to store Vassals info/config in `PostgreSQL`_ or `MongoDB`_


Some code is borrowed from projects I did earlier and some code is still not added yet, but does exists in my projects.

.. _PostgreSQL: http://uwsgi-docs.readthedocs.org/en/latest/ImperialMonitors.html#pg-scan-a-postgresql-table-for-configuration
.. _MongoDB: http://uwsgi-docs.readthedocs.org/en/latest/ImperialMonitors.html#mongodb-scan-mongodb-collections-for-configuration
