from django.contrib import admin  # noqa

from snippets.models import Snippet


@admin.register(Snippet)
class SnippetAdmin(admin.ModelAdmin):
    list_display = ('title', 'code',
                    'linenos', 'language', 'style', 'owner', 'highlighted')

    list_filter = ('language', 'style')

    fields = ['title', 'code', ('language', 'style')]
