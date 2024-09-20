from django.contrib import admin

# Register your models here.
from .models import *

class contactAdmin(admin.ModelAdmin):
    list_display=("name","contact","email","message")
admin.site.register(contact,contactAdmin)

class galleryAdmin(admin.ModelAdmin):
    list_display=("pdes","gpic","gdate",)
admin.site.register(gallery,galleryAdmin)

class recruitersAdmin(admin.ModelAdmin):
    list_display=("name","rpic","rdate",)
admin.site.register(recruiters,recruitersAdmin)

class coursesAdmin(admin.ModelAdmin):
    list_display=("id","cname","cpic","cdate",)
admin.site.register(courses,coursesAdmin)

class placementsAdmin(admin.ModelAdmin):
    list_display=("id","name","pcourse","branch","cmpname","cmplogo","city","pyear","designation","stupic","pdate")
admin.site.register(placements,placementsAdmin)

class factAdmin(admin.ModelAdmin):
    list_display=("cname","cpic","ccourse")
admin.site.register(fact,factAdmin)
