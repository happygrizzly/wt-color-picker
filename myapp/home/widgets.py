from django.forms import widgets, Media

from wagtail.telepath import register
from wagtail.widget_adapters import WidgetAdapter


class ColorPickerInput(widgets.TextInput):

    template_name = "home/color-picker-input.html"

    @property
    def media(self):
        return Media(
            css={
                'all': [
                    'css/color-picker.css',
                ]
            },
            js=[
                'js/color-picker.js',
                'js/color-picker-chooser.js'
            ]
        )


class ColorPickerInputAdapter(WidgetAdapter):

    js_constructor = "home.widgets.ColorPickerInput"

    class Media:
        js = [
            "wagtailadmin/js/telepath/widgets.js",
            "js/color-picker-widget-adapter.js",
        ]


register(ColorPickerInputAdapter(), ColorPickerInput)
