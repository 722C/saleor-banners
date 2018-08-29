# saleor-banners

Banner Plugin for [Saleor](https://github.com/mirumee/saleor)

This provides a (currently skeleton) implementation of banners. This is currently built for the `v2018.6` tag of Saleor.

Adding the banner as a separate model results in little to no internal changes to main Saleor code.

---

## Installation

To install, `pip install` the package as such:

```bash
pip install git+git://github.com/722c/saleor-banners.git#egg='saleor-banners'
```

Or list the package in your `requirements.txt` as such:

```
git+git://github.com/722c/saleor-banners.git#egg='saleor-banners'
```

Alternatively, this can be installed as a Git submodule directly in the root directory of your Saleor instance.

## Configuration

Once you have installed the app, you will need to add a few things to your project:

Add the app to your installed apps (the order doesn't matter):

```python
INSTALLED_APPS = [
    ...

    # Saleor plugins
    'saleor-banners.saleor_banners',

    ...
]
```

Add the apps URLs to your root `urls.py` in the `translatable_urlpatterns` near the bottom (this will allow any native Saleor URLs to be matched beforehand):

```python
translatable_urlpatterns = [
    ...
    url(r'^search/', include((search_urls, 'search'), namespace='search')),

    # URLs for saleor-banners
    url(r'', include('saleor-banners.saleor_banners.urls')),

    url(r'', include('payments.urls'))
]
```

Add the link to the dashboard by importing the template tag in `templates/dashboard/base.html` and putting it where you want in the side nav:

```django
<!DOCTYPE html>
{% load staticfiles i18n %}
 ...

 <!-- This is template tag you will need to load. -->
{% load saleor_banners_side_nav from saleor_banners %}

...

<ul class="side-nav">
  <li class="nav-home">
    <a href="{% url 'dashboard:index' %}">
      {% trans "Home" context "Dashboard homepage" %}
    </a>
  </li>
  {% if perms.product.view_product or perms.product.view_category %}
  <li class="side-nav-section" id="first">
    ...
  </li>
  {% endif %}

  <!-- Add in saleor-banners where you want. -->
  {% saleor_banners_side_nav %}

  ...
</ul>

...
```

Finally to add a banner to your page, add the template tag where you want. By default, it will center the text and have a width of `100%`.

```django
{% load saleor_banner_display from saleor_banners %}

...

<!-- Pass the name, which should match what is in the database. -->
<!-- If it doesn't match, it will render nothing. -->
{% load saleor_banner_display "Main" %}

...
```

To override the style, there are a couple of classes on the banner:

```css
.saleor-banner.saleor-banner-override {
  ...;
}
```
