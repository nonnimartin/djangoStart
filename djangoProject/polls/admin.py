# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
# these can then be created and modified in the admin UI

from django.contrib import admin

from .models import Question

admin.site.register(Question)