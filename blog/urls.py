from django.urls import path
from  .views import BlogListView, BlogDetailView, BlogCreateView, BlogEditView, BLogDeleteView

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('posts/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('posts/new/', BlogCreateView.as_view(), name='post_new'),
    path('posts/<int:pk>/edit/', BlogEditView.as_view(), name='post_edit'),
    path('posts/<int:pk>/delete/', BLogDeleteView.as_view(), name='post_delete'),
]