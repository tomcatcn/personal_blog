from django.conf.urls import url
from article.views import *


urlpatterns = [
    url(r'^list$',list_views),
    url(r'^details/(\d+)',details_view),
    url(r'^write',write_view),
    # url(r'^write/(\d+)',write_view),
    url(r'^write/submit',write_submit_view),

]