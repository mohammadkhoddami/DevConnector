from django.contrib import admin
from .models import Userprofile, AddEducation , Exp
# Register your models here.
admin.site.register(Userprofile)
admin.site.register(Exp)
admin.site.register(AddEducation)