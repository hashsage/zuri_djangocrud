from django.shortcuts import render

# Create your views here.

class PostListView(generic.ListView):
    model = Post
#    template_name = 'post_List.html'

class PostCreateView(generic.CreateView):
    model = Post
    fields="__all__"
    success_url  = reverse_lazy(“blog:all”)
#    template_name = 'post_Create.html'

class PostDetailView(generic.DetailView):
    model = Post


class PostUpdateView(generic.UpdateView):
    model = Post
    fields="__all__"
    success_url  = reverse_lazy(“blog:all”)


class PostDeleteView(generic.UpdateView):
    model = Post
    fields="__all__"
    success_url  = reverse_lazy(“blog:all”)

