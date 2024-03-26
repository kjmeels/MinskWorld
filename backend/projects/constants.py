from django.db.models import TextChoices


class ProjectChoices(TextChoices):
    BUSINESS = "Business", "Бизнес"
    DELUXE = "DeLuxe", "Делюкс"
    COMFORT = "Comfort", "Комфорт"
    COMFORTPLUS = "Comfort+", "Комфорт+"
