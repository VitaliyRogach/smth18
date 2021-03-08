from django.conf.urls import url
from .views import Data


urlpatterns = [
    url(r'^$', Data.as_view({'get' : 'index'})),
    url(r'^done/$', Data.as_view({'get' : 'done'})),

]