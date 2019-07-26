from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Paper, Underline, Score, Block, Block_Score, Memo,\
    Memo_Score, Comment, Comment_Score, Relationship

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Paper)
admin.site.register(Underline)
admin.site.register(Score)
admin.site.register(Block)
admin.site.register(Block_Score)
admin.site.register(Memo)
admin.site.register(Memo_Score)
admin.site.register(Comment)
admin.site.register(Comment_Score)
admin.site.register(Relationship)
