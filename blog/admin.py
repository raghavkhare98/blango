from django.contrib import admin
from blog.models import Tag, Post

admin.site.register(Tag)

"""
To customize admin site's behaviour for a model, we will create
a admin.ModelAdmin subclass.
"""
class PostAdmin(admin.ModelAdmin):
  prepopulated_fields = {"slug": ("title", )} #to automatically get the value of title in slug at the admin page
  exclude = ["created_at"] #will not allow them to be edited
  #list_display = [] list of fields to include in the admin page list view

admin.site.register(Post, PostAdmin)