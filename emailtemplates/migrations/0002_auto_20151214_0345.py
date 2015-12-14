# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('emailtemplates', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailtemplate',
            name='bcc',
            field=models.CharField(default=b'', help_text=b'Optional: specific a BCC address', max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='emailtemplate',
            name='slug',
            field=autoslug.fields.AutoSlugField(populate_from=b'name', editable=True, blank=True, unique=True),
        ),
    ]
