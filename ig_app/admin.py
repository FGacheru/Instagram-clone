from django.contrib import admin
from ig_app.models import Image, Comment, Preference

# Register your models here.
admin.site.register(Image)
admin.site.register(Comment)
admin.site.register(Preference)

