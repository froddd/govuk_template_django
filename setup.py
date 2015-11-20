#!/usr/bin/env python

import os
from setuptools import setup, find_packages

sdict = dict(
  name = 'django-govuk-template',
  packages = find_packages(),
  version = '0.16.0',
  description = 'Django packaged version of the GOV.UK template',
  long_description = 'A base template for Government Digital Services',
  url = 'https://github.com/alphagov/govuk_template',
  author = 'Government Digital Service developers (https://gds.blog.gov.uk/)',
  author_email = 'fred.marecesche@digital.justice.gov.uk',
  maintainer = 'Fred Marecesche',
  maintainer_email = 'fred.marecesche@digital.justice.gov.uk',
  keywords = ['python', 'django', 'alphagov', 'govuk'],
  license = 'MIT',
  include_package_data = True,
  install_requires = [
    'django>=1.3'
  ],
  platforms=["any"],
  classifiers=[
    'Programming Language :: Python',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Development Status :: 3 - Alpha',
    'Environment :: Web Environment',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Libraries :: Python Modules',
  ]
)

from distutils.core import setup
setup(**sdict)
