from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from agency.models import Redactor, Article, Topic


@admin.register(Redactor)
class RedactorAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("years_of_experience",)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_filter = ("topic",)


admin.site.register(Topic)
