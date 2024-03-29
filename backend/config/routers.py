from rest_framework.routers import DefaultRouter

from about_company.viewsets import AboutCompanyViewSet
from likes.viewsets import LikeViewSet
from main_page.viewsets import MainPageViewSet
from mortgage.viewsets import MortgageViewSet
from projects.viewsets import ProjectViewSet
from properties.viewsets import PropertyViewSet

router = DefaultRouter()

router.register("main_page", MainPageViewSet, basename="main_page")
router.register("projects", ProjectViewSet, basename="projects")
router.register("mortgages", MortgageViewSet, basename="mortgage")
router.register("properties", PropertyViewSet, basename="properties")
router.register("about_company", AboutCompanyViewSet, basename="about_company")
router.register("likes", LikeViewSet, basename="likes")
