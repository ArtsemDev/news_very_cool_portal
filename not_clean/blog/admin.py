from django.contrib import admin

from .models import Contact, Post


@admin.action(description='Опубликовать')
def make_published(self, request, queryset):
    queryset.update(is_published=True)


@admin.action(description='Снять с публикации')
def make_unpublished(self, request, queryset):
    queryset.update(is_published=False)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', 'subtitle')}
    list_display = ('title', 'author', 'date_published')
    date_hierarchy = 'date_published'
    list_filter = ('is_published', )
    readonly_fields = ('date_published', )
    actions = (make_published, make_unpublished)
    search_fields = ('title', 'id', 'subtitle')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'name')
    date_hierarchy = 'date_created'
    list_filter = ('email', )
    readonly_fields = ('email', 'name', 'message', 'date_created')
    search_fields = ('email', 'name', 'id')
