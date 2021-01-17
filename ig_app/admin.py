from django.contrib import admin
from ig_app.models import Post, Comment, Preference

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Preference)

