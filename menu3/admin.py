from django.contrib import admin
from menu3.models import Event, Register

class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'types',  'name', 'date','locality')
    list_display_links = ('id', 'name')
    list_filter = ['types']
    search_fields = ('id', 'name')
admin.site.register(Event, EventAdmin),

class RegisterAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name','email' ,'event')
    list_display_links = ('id', 'first_name')
    list_filter = ['event']
admin.site.register(Register, RegisterAdmin)