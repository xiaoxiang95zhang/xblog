from django.contrib import admin
from .models import BlogArticles


#admin.site.register(BlogArticles)

class BlogArticlesAdmin(admin.ModelAdmin):
    list_display = ("title", "auth", "publish")
    list_filter = ("publish", "auth")
    search_fields = ("title", "body")
    raw_id_fields = ("auth",)
    date_hierarchy = "publish"
    ordering = ['publish', 'auth']

admin.site.register(BlogArticles, BlogArticlesAdmin)
