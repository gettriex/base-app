from django import forms
from django.conf.global_settings import STATIC_ROOT, STATICFILES_DIRS
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe

from Baldezh.settings import BASE_DIR


class TagSelectWidget(forms.CheckboxSelectMultiple):
    template_name = 'catalog/widgets/tag_select.html'

    def render(self, name, value, attrs=None, renderer=None):
        context = self.get_context(name, value, attrs)
        context['widget']['attrs'].update({'class': 'tag-input'})
        html = render_to_string(self.template_name, context)
        return mark_safe(html)
