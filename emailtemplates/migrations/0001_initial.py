# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmailTemplate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=1024)),
                ('slug', autoslug.fields.AutoSlugField(unique=True, max_length=255, blank=True)),
                ('base_template', models.CharField(help_text=b"If present, the name of a django template.<br/> The body field will be present as the 'email_body' context variable", max_length=1024, blank=True)),
                ('subject', models.CharField(max_length=1024)),
                ('from_address', models.CharField(help_text=b"Specify as: 'Full Name &lt;email@address>'<br/>Defaults to: 'no-reply@site.domain'", max_length=1024, null=True, blank=True)),
                ('body', models.TextField(default=b'')),
                ('txt_body', models.TextField(help_text=b'If present, use as the plain-text body', null=True, blank=True)),
            ],
        ),
    ]
