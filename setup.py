# -*- coding: utf-8 -*-
import os
from setuptools import setup

setup(
        name='django-indisposable-email-field',
        version='0.1.6',
        packages=['indisposable_email_field'],
        include_package_data=True,
        url='https://github.com/sinnwerkstatt/django-indisposable-email-field',
        license='Apache License 2.0',
        author='Andreas Nüßlein',
        author_email='andreas.nuesslein@sinnwerkstatt.com',
        description='A Django form-Field that will check if the given email-address is a Disposable Email Address and block it accordingly.',
        setup_requires=['django'],
        classifiers=[
            'Development Status :: 4 - Beta',
            'Intended Audience :: Developers',
            'Programming Language :: Python',
        ]
)
