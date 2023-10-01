from django.urls import path
from . import views
urlpatterns = [
    path('btsfashion/', views.BtsFashionList.as_view(), name='btsfashion-list'),
    path('btsalbums/', views.BtsAlbumList.as_view(), name='btsalbums-list'),
    path('bt21/', views.BT21List.as_view(), name='bt21-list'),
    path('search/', views.ProducrSearchAPIView.as_view(), name='product-search'),
    # Add other URLs as needed
]
