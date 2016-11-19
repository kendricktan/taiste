from django.conf.urls import url
from demo.views import demo_view

urlpatterns = [
    url(r'^$', demo_view, name='demo_view')
]
