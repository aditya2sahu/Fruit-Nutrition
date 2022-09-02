from django.contrib import admin
from.models import Fruit
# Register your models here.
@admin.register(Fruit)
class adminfruit(admin.ModelAdmin):
    list_display = ["id","Name","Qunatity"]
