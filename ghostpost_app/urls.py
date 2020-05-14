from django.urls import path
from ghostpost_app import views


urlpatterns = [
    path('', views.index, name='homepage'),
    path('addpost/', views.addpost, name='addpost'),
    path('up_vote/<int:post_id>/', views.for_up_vote, name='up_vote'),
    path('down_vote/<int:post_id>/', views.for_down_vote, name='down_vote'),
]
