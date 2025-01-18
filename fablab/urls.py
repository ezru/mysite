from django.urls import path

from . import views

app_name = 'fablab'
urlpatterns = [
	path('', views.index, name='index'),
	path('<int:user_id>/', views.userdetails, name='userdetail'),
	path('<int:user_id>/booking', views.booking, name='userbooking'),
	path('booking', views.BookingPage.as_view(), name='fablabbooking'),
	path('about', views.AboutFablab.as_view(), name='aboutUs'),
	path('reserve', views.BookFablab.as_view(), name='reserve'),
	path('request', views.request_booking, name='request_booking'),
	path('confirmbooking', views.ConfirmBooking.as_view(), name='confirm_booking'),
]
