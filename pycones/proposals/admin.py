# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from proposals.actions import export_as_csv_action, send_confirmation_action
from proposals.models import ProposalSection, Proposal
from proposals.models import ProposalKind


@admin.register(Proposal)
class ProposalAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        "speaker",
        "speaker_email",
        "kind",
        "audience_level",
        "language",
        "get_avg",
        "get_reviews",
        "notified",
    ]
    list_filter = ["kind__name", "notified"]
    actions = [
        export_as_csv_action("CSV Export", fields=[
            "id",
            "title",
            "speaker",
            "speaker_email",
            "kind",
            "audience_level",
            "language",
            "avg_property",
            "reviews_property",
        ]),
        send_confirmation_action("Sends confirmation email")
    ]

    def get_avg(self, instance):
        return instance.avg()
    get_avg.short_description = _("Media")

    def get_reviews(self, instance):
        return instance.reviews_property
    get_reviews.short_description = _("Revisiones")

admin.site.register(ProposalSection)
admin.site.register(ProposalKind)
