from setuptools import setup, find_packages


VERSION = open('VERSION').read().lstrip('version: ').rstrip('\n')
setup(name='django-hospex',
     version = VERSION,
     packages=find_packages(),
     exclude_package_data={'rh2': ['bin/*.pyc']},
     setup_requires = ["setuptools_git >= 0.3",],
     scripts=['hospex/bin/manage.py'])
