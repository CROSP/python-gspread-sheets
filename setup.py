#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(name="python-gspread-sheets",
      description="This a sample project that shows how easily you can access"
                  " and manage Google Sheets documents in Python.",
      author="Alexander Molochko",
      author_email="alexander@crosp.net ",
      packages=find_packages(),
      url='https://github.com/CROSP/python-gspread-sheets',
      license="MIT License",
      classifiers=[
          "Intended Audience :: Developers",
          "Programming Language :: Python :: 3",
          "Topic :: Software Development :: Libraries :: Python Modules",
      ],
      platforms=["OS Independent"],
      install_requires=[
          "gspread>=3.0.0",
          "google",
          "google-auth"],
      )