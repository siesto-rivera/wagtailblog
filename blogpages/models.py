from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField
from wagtail.models import Page


class BlogIndex(Page):
    template = 'blogpages/blog_index.html'

    subtitle = models.CharField(max_length=100,  null=True)
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('body'),
    ]

class BlogDetail(Page):
    subtitle = models.CharField(max_length=100, null=True)
    body = RichTextField(blank=True, features=['h2', 'h3', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link'])

    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('body'),
    ]

