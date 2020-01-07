from django.contrib import admin
from menu4.models import Comment

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email')
    list_display_links = ('id', 'username')
    search_fields = ('id', 'username')
    
admin.site.register(Comment, CommentAdmin)