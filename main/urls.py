from django.urls import include, path

from .views import *

urlpatterns = [
    path("", index, name="home"),
    path("gallery/", GalleryListView.as_view(), name="gallery"),
    path("full-width/", full_width, name="full"),
    path("basic-grid/", basic_grid, name="basic-grid"),
    path("create-house/", create_house, name="create-house"),
    path("update-house/<int:pk>/", update_build, name="update-house"),
    path("about-us/", about_us, name="about-us"),
    # path('search_venues', PostListView.as_view(), name='search-venues'),
    path('baith_house', bait_house, name='bait-house-city'),
    path('spanish_house', spanish_house, name='spanish-house'),
    path('french_kvartal', french_kvartal, name='french-kvartal'),
    path('delete-house/<int:pk>/', delete_build, name='delete-house'),
    path('french_kvartal', french_kvartal, name='french-kvartal'),
]
