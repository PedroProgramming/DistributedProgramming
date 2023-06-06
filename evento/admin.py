from django.contrib import admin
from .models import InscricaoEvento

@admin.register(InscricaoEvento)
class RegisterUserEvento(admin.ModelAdmin):
    list_display = ('name', 'email',)
    readonly_fields = ('name', 'email',)
