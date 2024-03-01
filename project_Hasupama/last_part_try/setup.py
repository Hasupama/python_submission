# setup.py 
from setuptools import setup
setup(name='UU_tsp', 
      version='1.0', 
      description='Example package for The Traveling Salesperson Problem', 
      #url='https://github.com/uu-python/travis-fib', 
      author='Hasupama Jayasinghe', 
      #author_email='filipe.c.maia@gmail.com', 
      license='BSD',
      install_requires=[
            'random', 'cities'], # dependencies

      py_modules=['main','cities','__init__'],
      packages=[])