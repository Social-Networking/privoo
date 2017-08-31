from django.conf.urls import url
from .views import WallView, UserView, EditView

urlpatterns = [
    url(r'^$', WallView.as_view(), name='wall'),
    url(r'^(?P<pk>\w+)/$', UserView.as_view(), name='user'),
    url(r'^edit-profile/$', EditView.as_view(), name='edit-profile'),
]
