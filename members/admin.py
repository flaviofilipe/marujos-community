from django.contrib import admin
from .models import Member

class MemberAdmin(admin.ModelAdmin):
	list_display = ['name']
	ordering = ['name']

admin.site.register(Member, MemberAdmin)