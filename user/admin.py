from django.contrib import admin
from .models import TeacherModel,TeacherImageModel
# Register your models here.

class TeacherAdmin(admin.ModelAdmin):
    list_display=['username','mobile_no','education',]

    def username(self,obj):
        return f"{obj.user.username}"
admin.site.register(TeacherModel,TeacherAdmin)
admin.site.register(TeacherImageModel)