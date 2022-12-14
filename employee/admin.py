from django.contrib import admin
from .models import Employee, Department, Roles
from ckeditor.widgets import CKEditorWidget
# admin.py

# Register your models here.

admin.site.register(Employee)
admin.site.register(Department)
admin.site.register(Roles)

