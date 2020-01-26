from django.urls import path
from core import views
from core import temporary
urlpatterns = [
    path('', views.home, name='home'),
      path('new/member/',temporary.TickeCreateView.as_view(),name='m_create'),
      path('new/position/',temporary.PosCreateView.as_view(),name='p_create'),
      path('new/ins/',temporary.InsCreateView.as_view(),name='i_create'),
      path('member/<int:pk>/', temporary.member_detail, name='member_detail'),
]
