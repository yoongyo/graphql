from post.schema import Query as PostQuery
import graphene


class Query(PostQuery, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)