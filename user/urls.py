from django.conf.urls import url
from user.views import *
urlpatterns = [
    url(r'^login$',log_view),
    url(r'^reg$',reg_view),
    url(r'^logout',logout_view)

]