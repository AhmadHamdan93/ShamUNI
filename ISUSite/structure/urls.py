from django.urls import path
from . import views

app_name = 'structure'
urlpatterns = [
    path('', views.homepage, name="struct"),
    path('<slug:slug>', views.nav_detail, name='nav_detail'),
    path('newsList/', views.news_list_Page, name="news_page"),
    path('addsList/', views.ads_list_page, name="ads_page"),
    path('newsDetail/<int:id>/', views.news_detail_page, name="news_detail_page"),
    path('advertDetail/<int:id>/', views.advert_page, name="advert_detail_page"),
    path('gallery/', views.show_gallery, name="gallery_page"),
]
