from django.conf import settings
from graphene_django import DjangoObjectType

from .models import Post, Profile, Tag


class UserType(DjangoObjectType):
    class Meta:
        model = settings.AUTH_USER_MODEL

class AuthorType(DjangoObjectType):
    class Meta:
        model = Profile

class PostType(DjangoObjectType):
    class Meta:
        model = Post

class TagType(DjangoObjectType):
    class Meta:
        model = Tag
