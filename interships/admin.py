from django.contrib import admin
from .models import Intern, Role, RoleStatus

# Register your models here.
admin.site.register(Intern)
admin.site.register(Role)
admin.site.register(RoleStatus)