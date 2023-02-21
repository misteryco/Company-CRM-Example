from django.contrib import admin

from crm_for_companies.api_employees.models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'first_name', 'last_name', 'company')
