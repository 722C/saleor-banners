from django.utils.translation import npgettext, pgettext_lazy
from django_filters import (CharFilter, OrderingFilter)

from saleor.core.filters import SortedFilterSet

from ..models import SaleorBanner

SORT_BY_FIELDS = {
    'name': pgettext_lazy('Saleor banner list sorting option', 'name')}


class SaleorBannerFilter(SortedFilterSet):
    name = CharFilter(
        label=pgettext_lazy('Saleor banner list filter label', 'Name'),
        lookup_expr='icontains')
    sort_by = OrderingFilter(
        label=pgettext_lazy('Saleor banner list filter label', 'Sort by'),
        fields=SORT_BY_FIELDS.keys(),
        field_labels=SORT_BY_FIELDS)

    class Meta:
        model = SaleorBanner
        fields = []

    def get_summary_message(self):
        counter = self.qs.count()
        return npgettext(
            'Number of matching records in the dashboard banners list',
            'Found %(counter)d matching banner',
            'Found %(counter)d matching banners',
            number=counter) % {'counter': counter}
