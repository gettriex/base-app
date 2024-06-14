from django import forms
from django.conf.global_settings import STATIC_ROOT, STATICFILES_DIRS

from Baldezh.settings import BASE_DIR


class TagSelectWidget(forms.TextInput):
    template_name = 'widgets/tag_select.html'

    class Media:
        # js = (STATIC_ROOT / 'js/script.js',)
        js = (BASE_DIR / 'static/js/script.js',)
        css = {
            # 'all': (STATIC_ROOT / 'css/widgets.css',)
            'all': (BASE_DIR / 'static/css/widgets.css',)
        }
