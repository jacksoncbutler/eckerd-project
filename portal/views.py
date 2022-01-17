from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import View
from django.views import generic
from .forms import UserForm
from .models import Article, Class


class IndexView(generic.ListView):
    template_name = 'portal/index.html'
    context_object_name = 'articles'

    def get_queryset(self):
        return Article.objects.all()


class ArticleCreate(CreateView):
    model = Article
    fields = ['article_type', 'title', 'author', 'description', 'url']
    success_url = reverse_lazy('portal:index')


class ArticleUpdate(UpdateView):
    model = Article
    fields = ['article_type', 'title', 'author', 'description', 'url']
    success_url = reverse_lazy('portal:index')


class ArticleDelete(DeleteView):
    model = Article
    success_url = reverse_lazy('portal:index')


class LoginView(View):
    form_class = UserForm
    template_name = 'portal/login_form.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(None)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            # correct username and password login the user
            login(request, user)
            return redirect('portal:index')

        return render(request, self.template_name, {'form': form})
