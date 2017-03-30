from django.conf.urls import url
from views import current_datetime

urlpatterns = [
url(r'^$', current_datetime ),
]
