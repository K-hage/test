from django.conf import settings
from django.contrib import admin
from django.utils.safestring import mark_safe

from slider.models import Slider


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('image_preview', 'image_name')

    def image_preview(self, obj: Slider):
        # Вывод превью изображения
        return mark_safe(f'<img src="{settings.MEDIA_URL}{obj.image.file}" width="40" height="40">')

    def image_name(self, obj: Slider):
        # Вывод названия изображения
        return obj.image

    image_preview.short_description = ''
    image_name.short_description = 'Название'
