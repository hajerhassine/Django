from django.contrib import admin

from hub.models import Coach, Project, Student
from .models import Category, Product
# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Student)
admin.site.register(Coach)
admin.site.register(Project)

