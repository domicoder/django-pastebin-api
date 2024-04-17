from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import DefaultRouter

from snippets import views

# from rest_framework import renderers
# from snippets.views import api_root, SnippetViewSet, UserViewSet
# from rest_framework.urlpatterns import format_suffix_patterns


# # < start > API endpoints
# urlpatterns = [
#     # path('snippets/', views.snippet_list),
#     # path('snippets/<int:pk>/', views.snippet_detail),
#     path('', views.api_root),
#     # Snippets
#     path('snippets/', views.SnippetList.as_view()),
#     path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
#     # Users
#     path('users/', views.UserList.as_view()),
#     path('users/<int:pk>/', views.UserDetail.as_view()),
#     # Snippet highlights
#     path('snippets/<int:pk>/highlight', views.SnippetHighlight.as_view()),
# ]

# urlpatterns = format_suffix_patterns(urlpatterns)
# < end >

# < start > API endpoints with "Hyperlinking our API"
# urlpatterns = format_suffix_patterns([
#     path('', views.api_root),
#     path('snippets/',
#          views.SnippetList.as_view(),
#          name='snippet-list'),
#     path('snippets/<int:pk>/',
#          views.SnippetDetail.as_view(),
#          name='snippet-detail'),
#     path('snippets/<int:pk>/highlight/',
#          views.SnippetHighlight.as_view(),
#          name='snippet-highlight'),
#     path('users/',
#          views.UserList.as_view(),
#          name='user-list'),
#     path('users/<int:pk>/',
#          views.UserDetail.as_view(),
#          name='user-detail')
# ])
# < end >


# < start > Binding ViewSets to URLs
# Tutorial 6. Binding ViewSets to URLs explicitly
# snippet_list = SnippetViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# snippet_detail = SnippetViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
# snippet_highlight = SnippetViewSet.as_view({
#     'get': 'highlight'
# }, renderer_classes=[renderers.StaticHTMLRenderer])
# user_list = UserViewSet.as_view({
#     'get': 'list'
# })
# user_detail = UserViewSet.as_view({
#     'get': 'retrieve'
# })

# urlpatterns = format_suffix_patterns([
#     path('', api_root),
#     path('snippets/', snippet_list, name='snippet-list'),
#     path('snippets/<int:pk>/', snippet_detail, name='snippet-detail'),
#     path('snippets/<int:pk>/highlight/', snippet_highlight, name='snippet-highlight'),
#     path('users/', user_list, name='user-list'),
#     path('users/<int:pk>/', user_detail, name='user-detail')
# ])
# < end > Binding ViewSets to URLs


# < start > Using Routers
# DefaultRouter: automatically creates the API root view for us, so we can now delete the api_root
# Create a router and register our ViewSets with it.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet, basename='snippet')
router.register(r'users', views.UserViewSet, basename='user')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]

# Swagger UI -Documenting API-
schema_view = get_schema_view(
    openapi.Info(
        title="Pastebin API",
        default_version='v1',
        description="Simple Pastebin code highlighting Web API.",
        terms_of_service="https://www.django-rest-framework.org/tutorial/6-viewsets-and-routers/",
        contact=openapi.Contact(email="sanchezyander@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns += [
    path('api/doc/swagger/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path('api/doc/redoc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),
]
# < end > Using Routers
