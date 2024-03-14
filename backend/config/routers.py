from rest_framework.routers import DefaultRouter

from main_page.viewsets import MainPageViewSet

router = DefaultRouter()

router.register("main_page", MainPageViewSet, basename="main_page")
