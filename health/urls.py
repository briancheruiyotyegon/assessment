from django.urls import path
from . import views
urlpatterns=[
    path('users/', views.get_users, name='users'),
    path('users/user/<str:user_id>/', views.get_user, name='user'),
    path('users/search/<str:username>/', views.search_user_by_username, name='search_user_by_username'),
    path('users/create/', views.create_user, name='create_user'),
    path('users/update/<str:user_id>/', views.update_user, name='update_user'),
    path('users/delete/<str:user_id>/', views.delete_user, name='delete_user'),
    path('categories/', views.get_categories, name='categories'),
    path('categories/category/<str:category_id>/', views.get_category, name='category'),
    path('categories/search/<str:name>/', views.search_category_by_name, name='search_category_by_name'),
    path('categories/create/', views.create_category, name='create_category'),
    path('categories/update/<str:category_id>/', views.update_category, name='update_category'),
    path('categories/delete/<str:category_id>/', views.delete_category, name='delete_category'),
    path('data/', views.get_datas, name='data'),
    path('data/data/<str:data_id>/', views.get_data, name='data'),
    path('data/create/', views.create_data, name='create_data'),
    path('data/update/<str:data_id>/', views.update_data, name='update_data'),
    path('data/delete/<str:data_id>/', views.delete_data, name='delete_data'),
    path('data/search/<str:institution_name>/', views.search_data_by_institution_name, name='search_data_by_name'),
    path('data/search/<str:eventName>/', views.search_data_by_eventName, name='search_data_by_category'),
    path('data/search/<str:first_name>/', views.search_data_by_first_name, name='search_data_by_category'),
    path('data/search/<str:eventLocation>/', views.search_data_by_eventLocation, name='search_data_by_category'),
    path('data/search/<str:eventDate>/', views.search_data_by_eventDate, name='search_data_by_category'),



]
