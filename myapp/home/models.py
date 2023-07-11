from wagtail.admin.panels import FieldPanel

from wagtail.models import Page
from wagtail.fields import (
    StreamField
)

from .blocks import (
    JumboCard
)


class HomePage(Page):

    content = StreamField(
        [
            ('JumboCard', JumboCard()),
        ],
        use_json_field=True,
        blank=True,
        null=True
    )

    content_panels = Page.content_panels + [
        FieldPanel('content')
    ]
