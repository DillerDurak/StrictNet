from django.contrib import admin
from .models import *

admin.site.site_header = 'Администрирование StrictNet'

admin.site.register(User)
admin.site.register(Friend)
admin.site.register(Post)
admin.site.register(Message)
admin.site.register(Follower)
admin.site.register(Group)
admin.site.register(GroupMember)
admin.site.register(GroupFollower)
admin.site.register(GroupMessage)
admin.site.register(GroupMeta)
admin.site.register(GroupPost)