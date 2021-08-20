from django.conf.urls import url 
from src import views 
 
urlpatterns = [ 
    url(r'^api/reservation$', views.reservation_list),
    url(r'^api/tennis-court$', views.tennis_courts),
    url(r'^api/tutorial$', views.tutorial_list),
    # url(r'^api/tutorials/(?P<pk>[0-9]+)$', views.tutorial_detail),
    # url(r'^api/tutorials/published$', views.tutorial_list_published)
]
