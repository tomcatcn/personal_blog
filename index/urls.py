from django.conf.urls import url
from index.views import *
urlpatterns =[
    url(r'^$',index_view)
]