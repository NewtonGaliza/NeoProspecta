from django.urls import path, include
from neoprospecta import views
'''
from neospecta.views import EntryViewSet, api_root
from rest_framework import renderers
from rest_framework.urlpatterns import format_suffix_patterns
'''
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'entry', views.EntryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
