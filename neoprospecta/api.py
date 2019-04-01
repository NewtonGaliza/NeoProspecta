from rest_framework import routers
from core import views as core_views


router = routers.DefaultRouter()
router.register(r'entry', core_views.EntryViewSet)
