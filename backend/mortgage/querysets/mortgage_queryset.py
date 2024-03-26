from django.db.models import QuerySet, ExpressionWrapper, FloatField, F


class MortgageQuerySet(QuerySet):
    def annotate_month_payment(self, summ: int, term: int):
        return self.annotate(
            month_payment=ExpressionWrapper(
                int(summ) / int(term) / 12 * F("rate") / 100,
                output_field=FloatField(),
            )
        )
