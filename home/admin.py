from django.contrib import admin
from .models import Author, Genre, Diary

#admin.site.register(Diary)
#admin.site.register(Author)
admin.site.register(Genre)

# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'diary_count')
    def diary_count(self, obj):
        return obj.diary_set.count()
    
 # Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)



# Register the Admin classes for Book using the decorator

@admin.register(Diary)
class DiaryAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre', 'date')
    list_filter = ('author', 'genre')
    
