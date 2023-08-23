from django import forms
from django.utils.functional import cached_property
from django.utils.translation import gettext_lazy as _

from wagtail import blocks


class ColorPicker(blocks.FieldBlock):

    def __init__(self, required=True, help_text=None, validators=(), **kwargs):
        self.field_options = {
            "required": required,
            "help_text": help_text,
            "validators": validators,
        }
        super().__init__(**kwargs)

    @cached_property
    def field(self):
        from .widgets import ColorPickerInput
        field_kwargs = {
            "widget": ColorPickerInput(),
        }
        field_kwargs.update(self.field_options)
        return forms.CharField(**field_kwargs)


class ContentSectionBlockMixin(blocks.StructBlock):

    full_width = blocks.BooleanBlock(
        required=False,
        label=_('Use full width'),
        help_text=_('When selected `.container` will not be used')
    )

    spacer_top = blocks.BooleanBlock(
        required=False,
        label=_('Use top spacer'),
        help_text=_('Use predefined padding-top as a spacer')
    )

    spacer_bottom = blocks.BooleanBlock(
        required=False,
        label=_('Use bottom spacer'),
        help_text=_('Use predefined padding-bottom as a spacer')
    )

    background_color = ColorPicker(
        label=_('Background color'),
        help_text=_('Click on the text input to open the color dialog')
    )


class JumboCard(ContentSectionBlockMixin):

    title = blocks.TextBlock(
        required=True,
        label=_('Card title'),
    )

    class Meta:
        icon = 'link'
        verbose_name = _('Jumbo card')
        verbose_name_plural = _('Jumbo cards')
