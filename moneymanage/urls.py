from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index_mongmt'),
    path('rest/<int:guess>', views.rest),
    path('main', views.MainView.as_view()),
    path('remain/<slug:txting>', views.RestMainView.as_view()),
]