from blog.views import (CreatedByListView, PostListView, CategoryListViews,
                        page, post, SearchListView, TagListViews)
from django.urls import path

app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(), name='index'),
    path('post/<slug:slug>/', post, name='post'),
    path('page/<slug:slug>/', page, name='page'),
    path(
        'created_by/<int:author_pk>/',
        CreatedByListView.as_view(),
        name='created_by'
    ),
    path('category/<slug:slug>/', CategoryListViews.as_view(), name='category'),
    path('tag/<slug:slug>/', TagListViews.as_view(), name='tag'),
    path('search/', SearchListView.as_view(), name='search'),
]
