from django.contrib import admin

from . import models #from current directory import models.property

#enable django admin
admin.site.register(models.UserProfile)
admin.site.register(models.ProfileFeedItem)
