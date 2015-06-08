# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SavedSearch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('search_key', models.SlugField(help_text=b'A way to arbitrarily group queries. Should be a single word. Example: all-products', max_length=100)),
                ('user_query', models.CharField(help_text=b'The text the user searched on. Useful for display.', max_length=1000)),
                ('full_query', models.CharField(default=b'', help_text=b'The full query Haystack generated. Useful for searching again.', max_length=1000, blank=True)),
                ('result_count', models.PositiveIntegerField(default=0, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(related_name='saved_searches', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name_plural': 'Saved Searches',
            },
        ),
    ]
