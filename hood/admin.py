from django.contrib import admin

from hood.models import Business, Neighborhood, Profile


# Register your models here.
admin.site.register(Neighborhood)
admin.site.register(Business)
admin.site.register(Profile)