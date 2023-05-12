from django.urls import path
from . import views
from .views import UserListCreate, UserRetrieveUpdateDestroy, IndexView, UserUpdateView
app_name = 'users'

urlpatterns = [
    path('',IndexView.as_view(), name = 'index'),
    path('users/',UserListCreate.as_view(), name='create_user'), 
    path('users/<int:pk>/', UserRetrieveUpdateDestroy.as_view(), name='user_details'), 
    path('create/', views.create, name='create'),
    path('update/<int:pk>/', UserUpdateView.as_view(), name='update'),
    path('detail/<int:pk>/', views.StudDetail.as_view(), name='detail'),
    path('search-college/', views.CollegeSearchView.as_view(), name='search-data'),

]
