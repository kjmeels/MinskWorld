from django.db.models import QuerySet, Subquery, OuterRef


class ApartmentQuerySet(QuerySet):
    def annotate_max_floor(self):
        from ..models import Floor

        max_floor = Subquery(
            Floor.objects.all()
            .filter(entrance=OuterRef("entrance"))
            .order_by("-number")
            .values("number")[:1]
        )
        return self.annotate(max_floor=max_floor)
