from django.contrib import admin

from driver_model import models
# Register your models here.

class DriverAdmin(admin.ModelAdmin):
     list_display = (
        'id','full_name','gender','dob','contact','license_type')

admin.site.register(models.DriverDetail,DriverAdmin)
