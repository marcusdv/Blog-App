from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)
from . import views


urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    # Se for para post/1 por exemplo, vai apra o blog de id 1 graças ao: post<int:pk>
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'), #rota com variável
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'), 
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'), 
    path('about/', views.about, name='blog-about'),
]
