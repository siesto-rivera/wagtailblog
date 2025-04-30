from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField
from wagtail.models import Page


class BlogIndex(Page):
    template = 'blogpages/blog_index.html'
    max_count = 1
    parent_page_types = ['home.HomePage']
    subpage_types = ['blogpages.BlogDetail']

    subtitle = models.CharField(max_length=100,  null=True)
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('body'),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request)
        context['blogpages'] = BlogDetail.objects.live().public
        return context

class BlogDetail(Page):
    parent_page_types = ['blogpages.BlogIndex']
    subpage_types = []  #BlogDetail 의 child page 생성금지
    subtitle = models.CharField(max_length=100, null=True)
    body = RichTextField(blank=True, features=['h2', 'h3', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link'])

    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('body'),
    ]

