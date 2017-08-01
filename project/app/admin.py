# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Test
from advanced_filters.admin import AdminAdvancedFiltersMixin


# Register your models here.

@admin.register(Test)
class TestAdmin(AdminAdvancedFiltersMixin, admin.ModelAdmin):
    """
    """
    search_fields = ('test_1', )
