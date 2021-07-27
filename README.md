# drf_health_check
Various health check extensions for the Django Rest Framework

[![PyPI Version][pypi-image]][pypi-url]

[pypi-image]: https://img.shields.io/pypi/v/drf_health_check
[pypi-url]: https://pypi.org/project/drf_health_check/

# Installation

Using pip

`pip install drf_health_check`

Using pipenv

`pipenv install drf_health_check`

# Quick start
In your project’s `settings.py` add `HEALTH_CHECK_PROVIDERS`.

``` 
HEALTH_CHECK_PROVIDERS = {
    ...
    'drf_health_check.providers.DBHealthCheckProvider',
    ...
}
```

Add `drf_health_check` to `INSTALLED_APPS` 
```
INSTALLED_APPS = [
    ...
    "drf_health_check",
]
```

Add urls to you project for health-view
```
urlpatterns = [
    ...
    url("health/", include('django_health_check_view.urls')),
    ...
]
```