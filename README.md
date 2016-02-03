# django-indisposable-email-field
A Django form-Field that will check if the given email-address is a Disposable Email Address and block it accordingly.

## Quick start
1. Add "indisposable_email_field" to your INSTALLED_APPS setting like this:

        INSTALLED_APPS = [
            ...
            'indisposable_email_field',
        ]

2. Run `python manage.py migrate` to create the models and populate with blacklisted domains
3. Use `IndisposableEmailField` from `indisposable_email_field.fields` like any regular `EmailField`
4. Optional: Add more blacklisted domains in the django `/admin`
