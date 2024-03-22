from django.contrib import admin
from .models import TuitionModel
# Register your models here.

class TuitionAdmin(admin.ModelAdmin):
    list_display = ['grade','salary','location','day_perweek','available',]
    prepopulated_fields = {'grade_slug':('grade',),'location_slug':('location',)}
admin.site.register(TuitionModel,TuitionAdmin)