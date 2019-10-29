import graphene
from graphene_django.types import DjangoObjectType
from .models import Post


class PostType(DjangoObjectType):
    class Meta:
        model = Post


class Query(graphene.AbstractType):
    all_post = graphene.List(PostType)

    def resolve_all_posts(self, context, **kwargs):
        return Post.objects.all()
