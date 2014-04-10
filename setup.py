import os
from setuptools import setup, find_packages
from django_uwsgi import __version__


README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()


os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


setup(
    name='django-uwsgi',
    version=__version__,
    description='uWSGI stuff for Django projects',
    long_description=README,
    url='http://github.com/unbit/django-uwsgi',
    author='Eugene MechanisM',
    author_email='eugene@mechanism.name',
    license='MIT',
    #namespace_packages=['uwsgi', ],
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet :: WWW/HTTP :: WSGI',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
        'Topic :: Communications :: Email',
    ],
    keywords='uwsgi, django, mail, cache, template',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    extras_require={
        'uwsgi': ['uwsgi'],
    },
)
