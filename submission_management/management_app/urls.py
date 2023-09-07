from django.urls import path

from . import views

urlpatterns = [
	path('', views.ListIndexView.as_view()),
]