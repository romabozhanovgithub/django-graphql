from django.contrib.auth import get_user_model
from graphene_django import DjangoObjectType

from .models import Post, Profile, Tag

User = get_user_model()


class UserType(DjangoObjectType):
    class Meta:
        model = User

class AuthorType(DjangoObjectType):
    class Meta:
        model = Profile

class PostType(DjangoObjectType):
    class Meta:
        model = Post

class TagType(DjangoObjectType):
    class Meta:
        model = Tag
