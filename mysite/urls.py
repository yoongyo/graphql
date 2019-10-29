from django.contrib import admin
from django.urls import re_path
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True))),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)