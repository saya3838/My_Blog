#from django.shortcuts import render
from django.views.generic import ListView, DetailView
from blog.models import Post

class PostList(ListView):
  model = Post
  
  #ListViewで使われるHTMLのファイル名は、デフォルトでpost_list.htmlとなるが、例えばindex.htmlにしたい場合は、以下のようにする。
  template_name = "blog/index.html" 
  
  #変数object_listの名前を変更したいときは以下。
  context_object_name = "posts"

class PostDetail(DetailView):
  model = Post
  context_object_name = "post"