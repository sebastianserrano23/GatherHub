from django.contrib import admin

from gatherhub.core.models import Conference
from .models import Conference

admin.site.register(Conference)