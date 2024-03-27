from django.contrib import admin
from . models import Topic,Post,Comment,User,Contact

admin.site.register(Topic)
admin.site.register(User)
admin.site.register(Contact)
class Commentline(admin.StackedInline):
    model = Comment
    extra = 0
class PostAdmin(admin.ModelAdmin):
    inlines=[
        Commentline
    ]
admin.site.register(Post,PostAdmin)
