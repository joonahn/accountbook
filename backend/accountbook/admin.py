from django.contrib import admin
from .models import AccountBookData, Category
from mptt.admin import DraggableMPTTAdmin


class CategoryAdmin(DraggableMPTTAdmin):
    pass

# Register your models here.
admin.site.register(AccountBookData)
admin.site.register(Category, CategoryAdmin)
