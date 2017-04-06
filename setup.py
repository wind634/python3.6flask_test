#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name="flask_test",
    version="0.1.0",
    packages=find_packages(),
    zip_safe=False,
    
    description="egg test demo.",
    long_description="egg test demo, haha.",
    author="wind634",
    author_email="wind634@ossxp.com",
    
    license="GPL",
    keywords=("test", "egg"),
    platforms="Independant",
    url="",
    entry_points="""
     # -*- Entry points: -*-
     [abu.admin]
     flask_test = app.admin:Admin
     """,
)