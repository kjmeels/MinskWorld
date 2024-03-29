from django.contrib.admin import register
from solo.admin import SingletonModelAdmin
from ..models import AboutCompany


@register(AboutCompany)
class AboutCompanyAdmin(SingletonModelAdmin):
    pass
