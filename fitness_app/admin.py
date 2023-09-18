from django.contrib import admin
from .models import Trainer, Session


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'trainer_name', 'created_at')


admin.site.register(Trainer, CommentAdmin)
admin.site.register(Session)
