from django.contrib import admin
from .models import User, Question, FavoriteQuestion, ReadQuestion
# Register your models here.

admin.site.register(User)
admin.site.register(Question)
admin.site.register(FavoriteQuestion)
admin.site.register(ReadQuestion)