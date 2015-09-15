
# Django Email Templates

Email Templates is an open source Django app to allow creation and editing of email templates in Django's admin interface. The resulting templates can be referenced in code and will be rendered with standard Django template context.


## Installation

    pip install git+https://github.com/concentricsky/django-emailtemplates.git


Include Email Templates in your settings.py.

    INSTALLED_APPS = [

        ...

        'emailtemplates',

        ...
    ]

Send an email by using the send_email_template utility.

    from emailtemplates.utils import send_email_template
    send_email_template('template_slug', 'toemail@example.com', {'context_variable': 'foo'})


## Optional Settings

By default, the FROM address on emails will be `noreply` at the domain returned by Site.objects.get_current(). You can override that default in your settings.py:

    EMAILTEMPLATES_DEFAULT_FROM_EMAIL = 'noreply@yourdomain.com'

You can also implement DEBUG mode, where only email addresses that match your whitelist will receive emails.

    EMAILTEMPLATES_DEBUG = True
    EMAILTEMPLATES_DEBUG_WHITELIST = ['someone@yourdomain.com','anotherdomain.com',]



## License

This project is licensed under the Apache License, Version 2.0. Details can be found in the LICENSE.md file.


## About Concentric Sky

_For nearly a decade, Concentric Sky has been building technology solutions that impact people everywhere. We work in the mobile, enterprise and web application spaces. Our team, based in Eugene Oregon, loves to solve complex problems. Concentric Sky believes in contributing back to our community and one of the ways we do that is by open sourcing our code on GitHub. Contact Concentric Sky at hello@concentricsky.com._
