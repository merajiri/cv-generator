from django.contrib import admin
from pdf import models
admin.site.register(models.profile)
admin.site.site_header = "CV"
admin.site.index_title = "cv"