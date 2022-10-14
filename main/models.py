from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _


from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    email = models.EmailField(_('email address'),unique=True)
    middle_name = models.CharField(max_length=50)
    phoneNumber = PhoneNumberField(unique=True, null=True, blank=True)
    registeredAt = models.DateTimeField(auto_now_add=True)
    profile = models.CharField(max_length=80)
    intro = models.CharField(max_length=50)
    image = models.ImageField(upload_to='user_images/', default='user_images/default-user.png', blank=True, null=True)


    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Post(models.Model):
    userId = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    message = models.CharField(max_length=100)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Message(models.Model):
    sourceId = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='message')
    targetId = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='messageTarget')
    message = models.TextField(max_length=1000)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

    def __str__(self):
        return f'{self.sourceId} to {self.targetId}'

class Friend(models.Model):

    FRIEND_STATUS = [
        ('S','Shcool'),
        ('S','College'), 
        ('F','Family'), 
        ('CL','Close'), 
        ('A','Acquaintance'),
     ]

    sourceId = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='friend')
    targetId = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='friendTarget')
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices=FRIEND_STATUS, default='A')

    class Meta:
        verbose_name = 'Друг'
        verbose_name_plural = 'Друзья'


class Follower(models.Model):

    FOLLOWER_TYPE = [
        ('D','Dislike'),
        ('F','Follow'),
    ]

    sourceId = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='follower')
    targetId = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='followerTarget')
    type = models.CharField(max_length=1, choices=FOLLOWER_TYPE, default='F')
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Подписчик'
        verbose_name_plural = 'Подписчики'


class Group(models.Model):

    GROUP_TYPES = [
        ('A','Approved'),
        ('N','New'),
        ('B','Blocked'),
        ('A','Active'),
    ]


    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=75)
    metaTitle = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    status = models.CharField(max_length=1, choices=GROUP_TYPES, default='N')
    profile = models.TextField()
    summary = models.CharField(max_length=20)
    content = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'


class GroupMeta(models.Model):
    groupId = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='meta')
    key = models.CharField(max_length=50)
    content = models.TextField()


class GroupMember(models.Model):

    MEMBER_ROLES = [
        ('D','Default'),
        ('A','Admin'),
    ]

    MEMBER_STATUS = [
        ('N','New'),
        ('R','Rejected'),
        ('A','Active'),
        ('B','Blocked'),
    ]


    groupId = models.ForeignKey(Group, on_delete=models.CASCADE)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=1, choices=MEMBER_ROLES, default='D')
    status = models.CharField(max_length=1, choices=MEMBER_STATUS, default='D')
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    notes = models.TextField()

    class Meta:
        verbose_name = 'Член группы'
        verbose_name_plural = 'Члены группы'


class GroupFollower(models.Model):

    FOLLOWER_TYPE = [
        ('D','Dislike'),
        ('F','Follow'),
    ]

    groupId = models.ForeignKey(Group, on_delete=models.CASCADE)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=1, choices=FOLLOWER_TYPE)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Подписчик группы'
        verbose_name_plural = 'Подписчики группы'


class GroupMessage(models.Model):
    groupId = models.ForeignKey(Group, on_delete=models.CASCADE)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Сообщение группы'
        verbose_name_plural = 'Сообщения группы'


class GroupPost(models.Model):
    groupId = models.ForeignKey(Group, on_delete=models.CASCADE)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Пост группы'
        verbose_name_plural = 'Посты группы'
