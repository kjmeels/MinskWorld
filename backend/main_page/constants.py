from django.db.models import TextChoices


class ApartmentSelectionCategoriesChoices(TextChoices):
    BUSINESS = "Business", "Квартиры бизнесс-класса"
    NEAR_RIVER = "Near River", "Апартаменты у реки"
    VIEWS = "Apartments with view", "Апартаменты с видами"
