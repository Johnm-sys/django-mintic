from django.conf.urls import url 
from src import views 
 
urlpatterns = [ 
    url(r'^all/tennis-court/(?P<tennis_court>[0-9]+)$', views.tennis_reserve_all_list),
    url(r'^consult/tennis-court/(?P<tennis_court>[0-9]+)$', views.view_reserve_list),
    url(r'^client/tennis-court/(?P<tennis_court>[0-9]+)$', views.client_data),
    url(r'$', views.verify_serve)
]
