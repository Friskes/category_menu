from django.urls import path

from menu.views import MenuView


urlpatterns = [
    path('', MenuView.as_view(), name='home'),

    path('<slug:slug>/', MenuView.as_view(), name='menu')
]
