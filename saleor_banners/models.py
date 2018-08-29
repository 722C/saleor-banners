from django.conf import settings
from django.db import models

from django.utils.translation import pgettext_lazy

from versatileimagefield.fields import VersatileImageField

from saleor.core.permissions import MODELS_PERMISSIONS


# Add in the permissions specific to our models.
MODELS_PERMISSIONS += [
    'saleor_banners.view',
    'saleor_banners.edit'
]

DEFAULT_TEXT_COLOR = getattr(settings, 'DEFAULT_BANNER_TEXT_COLOR', '#f2ece7')
DEFAULT_BANNER_COLOR = getattr(settings, 'DEFAULT_BANNER_COLOR', '#ff473c')


class SaleorBanner(models.Model):
    name = models.CharField(max_length=255)
    banner_text = models.CharField(max_length=255)
    _text_color = models.CharField(max_length=7, default=DEFAULT_TEXT_COLOR)
    _banner_color = models.CharField(
        max_length=7, default=DEFAULT_BANNER_COLOR)
    added = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'saleor_banners'

        permissions = (
            ('view', pgettext_lazy('Permission description',
                                   'Can view banners')
             ),
            ('edit', pgettext_lazy('Permission description',
                                   'Can edit banners')))

    def __str__(self):
        return self.name

    @property
    def text_color(self):
        if len(self._text_color) != 7:
            if self._text_color[0] != '#':
                self._text_color = '#{}'.format(self._text_color)
            if len(self._text_color) == 4:
                self._text_color = '#{0}{0}{1}{1}{2}{2}'.format(
                    self._text_color[1], self._text_color[2],
                    self._text_color[3])
            elif len(self._text_color) != 7:
                self._text_color = DEFAULT_BANNER_COLOR
        return self._text_color

    @text_color.setter
    def text_color(self, value):
        if len(value) != 7:
            if value[0] != '#':
                value = '#{}'.format(value)
            if len(value) == 4:
                value = '#{0}{0}{1}{1}{2}{2}'.format(
                    value[1], value[2], value[3])
            elif len(value) != 7:
                value = DEFAULT_BANNER_COLOR
        self._text_color = value

    @property
    def banner_color(self):
        if len(self._banner_color) != 7:
            if self._banner_color[0] != '#':
                self._banner_color = '#{}'.format(self._banner_color)
            if len(self._banner_color) == 4:
                self._banner_color = '#{0}{0}{1}{1}{2}{2}'.format(
                    self._banner_color[1], self._banner_color[2],
                    self._banner_color[3])
            elif len(self._banner_color) != 7:
                self._banner_color = DEFAULT_TEXT_COLOR
            self.save()
        return self._banner_color

    @banner_color.setter
    def banner_color(self, value):
        if len(value) != 7:
            if value[0] != '#':
                value = '#{}'.format(value)
            if len(value) == 4:
                value = '#{0}{0}{1}{1}{2}{2}'.format(
                    value[1], value[2], value[3])
            elif len(value) != 7:
                value = DEFAULT_TEXT_COLOR
        self._banner_color = value
