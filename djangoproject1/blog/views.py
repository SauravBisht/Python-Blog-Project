from django.shortcuts import render
from .models import	Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


post = [
	{
		'author':'Saurav Bisht',
		'title':'Blog-Post 1',
		'date_posted':'January 7, 2019',
		'content': 'First Post'
	},

	{
		'author':'Vishakha Agarwal',
		'title':'Blog-Post 2',
		'date_posted':'January 8, 2019',
		'content': 'Second Post'
	}
]


def home (request):
	context={
		'posts': Post.objects.all(),
		'title': 'Home',
	}
	
	return render(request, 'blog/home.html', context)


class PostListView (LoginRequiredMixin, ListView):
	model = Post
	context_object_name = 'posts'
	template_name = 'blog/home.html'
	ordering = ['-date_posted']

class PostDetailView (DetailView):
	model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	# To check user is the current login user before updating// import UserPassesTestMixin
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False


class PostDeleteView (LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	success_url = '/blog/home/'

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False





def about (request):
	return render(request, 'blog/about.html', {'title': 'About'} )
