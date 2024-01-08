from django.contrib import admin
from django.utils.html import format_html

from .models import Bookmark


# Register your models here.
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ("show_title", "description", "is_public", "user", "tag_list")
    list_filter = ("is_public", "user")
    search_fields = ("url", "description")
    ordering = ("url",)

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related("tags")

    def tag_list(self, obj):
        return ", ".join(o.name for o in obj.tags.all())

    tag_list.short_description = "Tags"


    def show_title(self, obj):
        return format_html('<a href="{}" target="_blank">{}</a>', obj.url, obj.title)

    show_title.short_description = "Title"


admin.site.register(Bookmark, BookmarkAdmin)
