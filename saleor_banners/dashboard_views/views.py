from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404, redirect
from django.template.response import TemplateResponse
from django.utils.translation import pgettext_lazy

from saleor.core.utils import get_paginator_items
from saleor.dashboard.views import staff_member_required
from .filters import SaleorBannerFilter
from .forms import SaleorBannerForm

from ..models import SaleorBanner


@staff_member_required
@permission_required('saleor_banners.view')
def saleor_banner_list(request):
    saleor_banners = (
        SaleorBanner.objects.all().order_by('name'))
    saleor_banner_filter = SaleorBannerFilter(
        request.GET, queryset=saleor_banners)
    saleor_banners = get_paginator_items(
        saleor_banner_filter.qs, settings.DASHBOARD_PAGINATE_BY, request.GET.get('page'))
    # Call this so that cleaned_data exists on the filter_set
    saleor_banner_filter.form.is_valid()
    ctx = {
        'saleor_banners': saleor_banners, 'filter_set': saleor_banner_filter,
        'is_empty': not saleor_banner_filter.queryset.exists()}
    return TemplateResponse(request, 'saleor_banners/dashboard/list.html', ctx)


@staff_member_required
@permission_required('saleor_banners.edit')
def saleor_banner_create(request):
    saleor_banner = SaleorBanner()
    form = SaleorBannerForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        msg = pgettext_lazy('Dashboard message', 'Created banner')
        messages.success(request, msg)
        return redirect('saleor-banner-dashboard-list')
    ctx = {'saleor_banner': saleor_banner, 'form': form}
    return TemplateResponse(request, 'saleor_banners/dashboard/detail.html', ctx)


@staff_member_required
@permission_required('saleor_banners.edit')
def saleor_banner_details(request, pk):
    saleor_banner = SaleorBanner.objects.get(pk=pk)
    form = SaleorBannerForm(
        request.POST or None, request.FILES or None, instance=saleor_banner)
    if form.is_valid():
        form.save()
        msg = pgettext_lazy(
            'Dashboard message', 'Updated banner %s') % saleor_banner.name
        messages.success(request, msg)
        return redirect('saleor-banner-dashboard-list')
    ctx = {'saleor_banner': saleor_banner, 'form': form}
    return TemplateResponse(request, 'saleor_banners/dashboard/detail.html', ctx)


@staff_member_required
@permission_required('saleor_banners.edit')
def saleor_banner_delete(request, pk):
    saleor_banner = get_object_or_404(SaleorBanner, pk=pk)
    if request.method == 'POST':
        saleor_banner.delete()
        msg = pgettext_lazy('Dashboard message',
                            'Removed banner %s') % saleor_banner
        messages.success(request, msg)
        return redirect('saleor-banner-dashboard-list')
    return TemplateResponse(
        request, 'saleor_banners/dashboard/modal/confirm_delete.html', {'saleor_banner': saleor_banner})
