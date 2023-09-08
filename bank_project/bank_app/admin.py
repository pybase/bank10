from django.contrib import admin

from bank_app.models import Bank, Members

# Register your models here.
admin.site.register(Bank)
admin.site.register(Members)