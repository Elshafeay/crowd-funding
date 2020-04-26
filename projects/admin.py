from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Project)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Review)
admin.site.register(Comment)
admin.site.register(Donation)
admin.site.register(FeaturedProject)
admin.site.register(SavedProject)
admin.site.register(ProjectTags)
admin.site.register(ProjectImages)
admin.site.register(Reply)
