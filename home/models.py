from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.documents import get_document_model
from wagtail.fields import RichTextField
from wagtail.images import get_image_model

from wagtail.models import Page


class HomePage(Page):
    max_count = 1
    subtitle = models.CharField("부제",max_length=100, blank=True, null=True)
    body = RichTextField(blank=True)
    image = models.ForeignKey(
        get_image_model(),  # 'wagtailimages.Image' can be used as a string
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    custom_document = models.ForeignKey(
        get_document_model(),
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    content_panels = Page.content_panels + [
        FieldPanel("subtitle", read_only=True),
        FieldPanel("body"),
        FieldPanel("image"),
        FieldPanel("custom_document"),
    ]
