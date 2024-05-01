from django.contrib import admin
from .models import ArticleCategory, Article

# Register your models here.

class ArticleInLine(admin.TabularInline):
    model = Article


class ArticleCategoryAdmin(admin.ModelAdmin):
    model = ArticleCategory
    inlines = [ArticleInLine,]

    search_fields = ['name',]
    list_display = ['name',]
    list_filter = ['name',]


class ArticleAdmin(admin.ModelAdmin):
    model = Article

    search_fields = ['title',]
    list_display = ['title', 'category']
    list_filter = ['title',]


admin.site.register(ArticleCategory, ArticleCategoryAdmin)
admin.site.register(Article, ArticleAdmin)

