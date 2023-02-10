from django.contrib import admin
from .models import Book, Author, Genre


class SlugModelAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)


admin.site.register(Book, SlugModelAdmin)
admin.site.register(Author, SlugModelAdmin)
admin.site.register(Genre, SlugModelAdmin)
