from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cars/', views.cars_index, name='index'),
    path('cars/<int:car_id/', views.cars_detail, name='detail'),
    path('cars/create/', views.CarCreate.as_view(), name='cars_create'),
    path('cars/<int:pk>/update/', views.CarUpdate.as_view(), name='cars_update'),
    path('cars/<int:pk>/delete/', views.CarDelete.as_view(), name='cars_delete'),
    path('cars/<int:car_id>/add_tire/', views.add_tire, name='add_tire'),
    path('rims/', views.RimList.as_view(), name='rims_index'),
    path('rims/<int:pk>/', views.RimDetail.as_view(), name='rims_detail'),
    path('rims/create/', views.RimCreate.as_view(), name='rims_create'),
    path('rims/<int:pk>/update/', views.RimUpdate.as_view(), name='rims_update'),
    path('rims/<int:pk>/delete/', views.RimDelete.as_view(), name='rims_delete'),
    path('cars/<int:car_id>/assoc_rim/<int:rim_id>/', views.assoc_rim, name='assoc_rim')

]