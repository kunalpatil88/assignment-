from django.urls import path
from . import views

urlpatterns = [
    path('get_data/', views.get_data, name='get_data'),
    path('make_prediction/', views.make_prediction, name='make_prediction'),
    path('model_interaction/', views.model_interaction, name='model_interaction'),
]
