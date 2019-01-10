from django.urls import path
from . import views
from users import views as users_views
from django.contrib.auth import views as auth_views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [


	path('', PostListView.as_view(), name = 'blog-home'),# list view of post in home page
	path('post/<int:pk>/', PostDetailView.as_view(), name = 'post-detail'), # individual details of the post
	path('post/new/', PostCreateView.as_view(), name = 'post-create'), # new post
	path('post/<int:pk>/update', PostUpdateView.as_view(), name = 'post-update'),
	path('post/<int:pk>/delete', PostDeleteView.as_view(), name = 'post-delete'),
	path('about/', views.about, name = 'blog-about'),
	path('register/', users_views.register, name='users_register'),
	path('profile/', users_views.profile, name='profile'),
	path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
	path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),

]