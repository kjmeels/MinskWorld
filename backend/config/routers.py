from rest_framework.routers import DefaultRouter

from main_page.viewsets import MainPageViewSet
from projects.viewsets import ProjectViewSet

router = DefaultRouter()

router.register("main_page", MainPageViewSet, basename="main_page")
router.register("projects", ProjectViewSet, basename="projects")
