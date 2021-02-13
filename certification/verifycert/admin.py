from django.contrib import admin

from .models import Year, Events, Certificate

admin.site.register(Year)
admin.site.register(Events)
admin.site.register(Certificate)