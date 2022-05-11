from django.contrib import admin
from .models import Post, Group


class PostAdmin(admin.ModelAdmin):
    # поля, которые должны отображаться в админке
    list_display = (
        'pk',
        'text',
        'pub_date',
        'author',
        'group'
    )
    # возможность изменять group в любом посте
    list_editable = ('group',)
    # интерфейс для поиска по тексту постов
    search_fields = ('text',)
    # возможность фильтрации по дате
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


# При регистрации модели Post источником конфигурации для неё назначаем
# класс PostAdmin
admin.site.register(Post, PostAdmin)
admin.site.register(Group)
