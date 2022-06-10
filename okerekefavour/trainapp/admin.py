from django.contrib import admin
from .models import Company, Company_employee, States

# Register your models here.
admin.site.register(Company)
admin.site.register(Company_employee)
admin.site.register(States)