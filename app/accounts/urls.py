from django.urls import path
from accounts import views


urlpatterns = [
    path('create', views.CreateUserView.as_view(), name='user-create'),
    path('login', views.LoginUserView.as_view(), name='user-login'),
    path('logout', views.LogoutUserView.as_view(), name='user-logout'),
    path('profile/<str:pk>',
         views.ProfileDetailView.as_view(),
         name='profile-detail'),
]
