from django.shortcuts import render
from django.views import generic
from .models import Post
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView, LogoutView
from blog.models import Post
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.forms import UserCreationForm

def index(request):
    my_dict = {"insert_me": "I am from views.py"}
    return render(request,'index.html',context=my_dict)


class PostList(ListView):
    model = Post
    template_name = 'index.html'

class PostDetail(DetailView):
    model = Post
    template_name = 'blog_detail.html'



class BlogCreate(LoginRequiredMixin, CreateView):

    model = Post
    template_name = 'blogmodel_form.html'
    success_url = reverse_lazy("home")
    fields = ["titulo","sub_titulo", "cuerpo", "imagen"]

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)


class BlogUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):

    model = Post
    template_name = 'blogmodel_form.html'
    success_url = reverse_lazy("home")
    fields = ["titulo", "sub_titulo", "cuerpo", "imagen"]

    def test_func(self):
        exist = Post.objects.filter(autor=self.request.user.id, id=self.kwargs['pk'])
        return True if exist else False
        


class BlogDelete(LoginRequiredMixin,UserPassesTestMixin, DeleteView):

    model = Post
    template_name = 'blogmodel_confirm_delete.html'
    success_url = reverse_lazy("home")

    def test_func(self):
        exist = Post.objects.filter(autor=self.request.user.id, id=self.kwargs['pk'])
        return True if exist else False


class BlogLogin(LoginView):
    template_name = 'blog_login.html'
    next_page = reverse_lazy("home")


class BlogLogout(LogoutView):
    template_name = 'blog_logout.html'

class About(TemplateView):
    template_name = 'about.html'

    
    

