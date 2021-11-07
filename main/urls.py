from django.urls import path
from .views import HomeView, ArticleViews, AddPost, EditView, DeleteArticle

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticleViews.as_view(), name='article'),
    path('new_post/', AddPost.as_view(), name='New post'),
    path('article/edit/<int:pk>', EditView.as_view(), name='Edit post'),
    path('article/<int:pk>/delete', DeleteArticle.as_view(), name='Delete'),
]