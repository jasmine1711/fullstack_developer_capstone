from django.urls import path
from . import views  # .views gives access to login_view and logout_view

app_name = 'djangoapp'

urlpatterns = [
    # Auth routes
    path("login/", views.login_user, name="login"),

    path('logout/', views.logout_view, name='logout'),
    
    path('register/', views.register_user, name='register'),
    # Add other views here (e.g., registration, review)
    # path('register', views.register_view, name='register'),
    # path('add_review', views.add_review_view, name='add_review'),
]

