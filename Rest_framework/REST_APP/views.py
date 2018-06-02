from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from rest_framework import viewsets
from Rest_framework.REST_APP.serializers import ArticleSerializer
from .models import Article
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.template import RequestContext, loader
from forms import ArticleForm
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect


class ArticleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Article.objects.order_by('vote')
    serializer_class = ArticleSerializer
    
    
def index(request):
    return render(request, 'article.html')

def article_new(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('article')
    else:
        form = ArticleForm()
    return render(request, 'new_article.html', {'form': form})