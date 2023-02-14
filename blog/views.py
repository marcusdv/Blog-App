from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post


# urls patterns mandam para views, que são essas funções,
# então as views lidam com a lógica para as rotas 
# então renderizam as templates

# essa não está sendo utilizda
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    # primeiro argumento é o objeto request, segundo template name que quer carregar, 3° vai passar os dados e permitir utiliza-los na template
    return render(request, 'blog/home.html', context)


# essa está sendo utilizada
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted'] # ordena os posts de acordo com a data. 


class PostDetailView(DetailView): # will search for blog/post_detail.html
    model = Post 


class PostCreateView(LoginRequiredMixin, CreateView):  # will search for blog/post_form.html
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
    
   
    def test_func(self):  # prevenir que qualquer ume edite qualquer post de outros usuários
        post = self.get_object() # pega o post atual 
        if self.request.user == post.author: # pega o usuario atual e checa com o author do post
            return True
        return False
    
    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = "/"

    def test_func(self):  # prevenir que qualquer ume apague qualquer post de outros usuários
        post = self.get_object() # pega o post atual 
        if self.request.user == post.author: # pega o usuario atual e checa com o author do post
            return True
        return False
    
def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})