from django.urls import path, include
from django.views.decorators.cache import cache_page
from .views import *

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    # path('', index, name='home'),
    path('', HomeNews.as_view(), name='home'),
    # path('', cache_page(60*1)(HomeNews.as_view()), name='home'), #Вариант с кешированием
    # path('category/<int:category_id>/', get_category, name='category'),
    path('category/<int:category_id>/', NewsCategory.as_view(), name='category'),
    # path('news/<int:news_id>/', show_news, name='show_news'),
    path('news/<int:pk>/', ShowNews.as_view(), name='show_news'),
    # path('news/add-news/', add_news, name='add_news'),
    path('news/add-news/', CreateNews.as_view(), name='add_news'),
    path('conntact/', contact, name='contact'),
    path('captcha/', include('captcha.urls')),

]
