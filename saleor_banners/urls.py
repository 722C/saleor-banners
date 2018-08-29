from django.conf.urls import url

from .dashboard_views import views as dashboard_views

urlpatterns = [
    url(r'^dashboard/banners/$',
        dashboard_views.saleor_banner_list,
        name='saleor-banner-dashboard-list'),
    url(r'^dashboard/banners/create/$',
        dashboard_views.saleor_banner_create,
        name='saleor-banner-dashboard-create'),
    url(r'^dashboard/banners/(?P<pk>[0-9]+)/$',
        dashboard_views.saleor_banner_details,
        name='saleor-banner-dashboard-detail'),
    url(r'^dashboard/banners/(?P<pk>[0-9]+)/delete/$',
        dashboard_views.saleor_banner_delete,
        name='saleor-banner-dashboard-delete'),
]
