from django.contrib import admin

from django import forms
from .models import News, Category
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class NewsAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = News
        fields = '__all__'


class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm
    list_display = (
        'id', 'title', 'category', 'created_at', 'updated_at',
        'is_published')  # форимрование отображение таблицы для админки
    list_display_links = ('id', 'title')
    search_fields = ('title', "created_at")
    list_editable = ('is_published',)  # изменение статуса из админки
    list_filter = ('created_at', 'category')  # настраиваемый поиск в админке


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title')  # форимрование отображение таблицы для админки
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
