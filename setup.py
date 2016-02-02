# -*- coding: utf-8 -*-
from setuptools import setup

setup(
        name='django-indisposable-email-field',
        version='0.1',
        packages=['indisposable_email_field'],
        url='https://github.com/sinnwerkstatt/django-indisposable-email-field',
        license='Apache License 2.0',
        author='Andreas Nüßlein',
        author_email='andreas.nuesslein@sinnwerkstatt.com',
        description='A Django form-Field that will check if the given email-address is an Disposable Email Address.',
        classifiers=[
            'Intended Audience :: Developers',
            'Programming Language :: Python',
        ]
)
