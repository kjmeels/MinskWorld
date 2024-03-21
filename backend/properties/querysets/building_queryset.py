from django.db.models import QuerySet, Count, Q, BooleanField, Case, When, Min

from properties.constants import RoomsCountChoices, StatusChoices


class BuildingQuerySet(QuerySet):
    """Менеджер домов."""

    def annotate_has_furnish(self):
        return self.annotate(
            has_furnish_apartments_count=Count("apartments", filter=Q(apartments__furnish=True))
        ).annotate(
            has_furnish=Case(
                When(has_furnish_apartments_count__gt=0, then=True),
                default=False,
                output_field=BooleanField(),
            )
        )

    def annotate_studio_min_price(self):
        return self.annotate(
            studio_min_price=Min(
                "apartments__price",
                filter=Q(
                    apartments__room_count=RoomsCountChoices.STUDIO,
                    apartments__status=StatusChoices.FREE,
                ),
            )
        )

    def annotate_one_room_min_price(self):
        return self.annotate(
            one_room_min_price=Min(
                "apartments__price",
                filter=Q(
                    apartments__room_count=RoomsCountChoices.ONE_ROOM,
                    apartments__status=StatusChoices.FREE,
                ),
            )
        )

    def annotate_two_room_min_price(self):
        return self.annotate(
            two_room_min_price=Min(
                "apartments__price",
                filter=Q(
                    apartments__room_count=RoomsCountChoices.TWO_ROOM,
                    apartments__status=StatusChoices.FREE,
                ),
            )
        )

    def annotate_three_room_min_price(self):
        return self.annotate(
            three_room_min_price=Min(
                "apartments__price",
                filter=Q(
                    apartments__room_count=RoomsCountChoices.THREE_ROOM,
                    apartments__status=StatusChoices.FREE,
                ),
            )
        )

    def annotate_four_room_min_price(self):
        return self.annotate(
            four_room_min_price=Min(
                "apartments__price",
                filter=Q(
                    apartments__room_count=RoomsCountChoices.FOUR_ROOM,
                    apartments__status=StatusChoices.FREE,
                ),
            )
        )

    def annotate_five_room_min_price(self):
        return self.annotate(
            five_room_min_price=Min(
                "apartments__price",
                filter=Q(
                    apartments__room_count=RoomsCountChoices.FIVE_ROOM,
                    apartments__status=StatusChoices.FREE,
                ),
            )
        )

    def annotate_six_room_min_price(self):
        return self.annotate(
            six_room_min_price=Min(
                "apartments__price",
                filter=Q(
                    apartments__room_count=RoomsCountChoices.SIX_ROOM,
                    apartments__status=StatusChoices.FREE,
                ),
            )
        )

    def annotate_count_free_apartments(self):
        return self.annotate(
            count_free_apartments=Count(
                "apartments", filter=Q(apartments__status=StatusChoices.FREE)
            )
        )
