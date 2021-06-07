from django.contrib import admin
from .models import Accounts

class AccountsAdmin(admin.ModelAdmin):
    list_display=('username','servername','password')

admin.site.register(Accounts,AccountsAdmin)