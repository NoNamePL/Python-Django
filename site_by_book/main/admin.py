from django.contrib import admin

from .models import NewsCart


class NewCartAdmin(admin.ModelAdmin):
    #   fields = ['title', 'image', 'content', 'published']
    list_display = ("title", "content", "published")
    list_display_links = ("title", "content")
    search_fields = ("title", "content", )


admin.site.register(NewsCart, NewCartAdmin)
