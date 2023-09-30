from django.contrib import admin

from .models import Conference

register_these = [Conference]

for these_nuts in register_these:
    admin.site.register(these_nuts)

