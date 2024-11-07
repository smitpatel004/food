from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Receipe)
admin.site.register(Student)
admin.site.register(Department)
admin.site.register(StudentId)
admin.site.register(Subject)
class SubjectMarkAdmin(admin.ModelAdmin):
    list_display=['student','Subject','marks']
admin.site.register(SubjectMarks,SubjectMarkAdmin)