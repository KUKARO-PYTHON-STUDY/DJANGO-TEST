from django.contrib import admin

from burgers.models import Burger

# Register your models here.


@admin.register(Burger)
class BurgetAdmin(admin.ModelAdmin):
    pass
