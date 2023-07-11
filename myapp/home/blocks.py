from django import forms
from django.utils.functional import cached_property
from django.utils.translation import gettext_lazy as _

from wagtail import blocks
from wagtail.blocks.struct_block import StructBlockAdapter

from wagtail.telepath import register as register_telepath_adapter


class ColorPicker(blocks.FieldBlock):
    def __init__(self, required=True, help_text=None, **kwargs):
        self.field = forms.CharField(required=required, help_text=help_text)
        super().__init__(**kwargs)


class ColorPickerAdapter(StructBlockAdapter):

  js_constructor = 'core.blocks.ColorPicker'

  @cached_property
  def media(self):
    structblock_media = super().media
    return forms.Media(
      css={
        'all': [
          'admin/css/plugins/color-picker.css',
        ]
      },
      js=structblock_media._js + [
        'admin/js/plugins/color-picker.js',
        'admin/js/core/blocks/color-picker-adapter.js'
      ]
    )


register_telepath_adapter(ColorPickerAdapter(), ColorPicker)


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
    template = 'core/blocks/JumboCard.html'
    verbose_name = _('Jumbo card')
    verbose_name_plural = _('Jumbo cards')