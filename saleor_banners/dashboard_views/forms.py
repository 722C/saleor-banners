from django import forms
from django.forms.widgets import TextInput
from django.db.models import Q
from django.utils.translation import pgettext_lazy

from saleor.product.models import Category
from ..models import SaleorBanner


class SaleorBannerForm(forms.ModelForm):

    text_color = forms.CharField(widget=TextInput(attrs={'type': 'color'}))
    banner_color = forms.CharField(widget=TextInput(attrs={'type': 'color'}))

    class Meta:
        model = SaleorBanner
        verbose_name_plural = 'banners'
        fields = ['name', 'banner_text']

    def __init__(self, *args, **kwargs):
        super(SaleorBannerForm, self).__init__(*args, **kwargs)
        self.fields['text_color'].initial = self.instance.text_color
        self.fields['banner_color'].initial = self.instance.banner_color

    def save(self, commit=True):
        instance = super(SaleorBannerForm, self).save(commit=commit)
        instance.text_color = self.cleaned_data.get('text_color', '')
        instance.banner_color = self.cleaned_data.get('banner_color', '')
        if commit:
            instance.save()
        return instance
