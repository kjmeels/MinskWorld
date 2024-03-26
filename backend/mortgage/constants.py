from django.db.models import TextChoices


class MortgageChoices(TextChoices):
    STANDART = "Standart", "Стандартный"
    FAMILY = "Families", "Семейная"
    ARMY = "Army", "Военная"
    GOVERMENT = "Government", "Государственная"
