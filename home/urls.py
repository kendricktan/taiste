from django.conf.urls import url
from home.views import home_view

urlpatterns = [
    url(r'^$', home_view, name='home_view')
]
