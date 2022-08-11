from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from .models import News, Category
from .forms import NewsForm, UserRigisterForm, UserLoginForm, ContactForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import login, logout
from django.core.mail import send_mail


# Create your views here.
def register(request):
    if request.method == 'POST':  # проверка на метод
        form = UserRigisterForm(request.POST)
        if form.is_valid():  # если форма валидна save
            user = form.save()
            login(request, user)  # автоматический вход
            messages.success(request, "Вы успешно зарегистрированы ")
            return redirect('home')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRigisterForm()

    context = {'form': form}
    return render(request, 'news/register.html', context)


def contact(request):
    if request.method == 'POST':  # проверка на метод
        form = ContactForm(request.POST)
        if form.is_valid():  # если форма валидна save
            mail = send_mail(form.cleaned_data['subject'], form.cleaned_data['content'], 'testmailsite2@gmail.com',
                      ['allstones.black@gmail.com'], fail_silently=False)
            if mail:
                messages.success(request, "Письмо отправлено")
                return redirect('home')
            else:
                messages.error(request, 'Ошибка отправки')
        else:
            messages.error(request, 'Ошибка отправки')
    else:
        form = ContactForm()

    context = {'form': form}
    return render(request, 'news/contact.html', context)


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)  # не забыдт про аттрибут data
        if form.is_valid():  # если форма валидна save
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'news/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('home')


class HomeNews(ListView):
    model = News
    template_name = 'news/news_list.html'
    context_object_name = 'news'  # по сути ренейм object_list в  объект news
    paginate_by = 3

    # extra_context = {'title': 'Главная'} #Не рекомендуется использование, только для статичных данных
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)  # не затереть предыдущее значение
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True).select_related(
            'category')  # Select_related выводит все запросы, точно нужные


class NewsCategory(ListView):  # получаем набор данных через супер класс
    model = News
    template_name = 'news/new_list.html'
    context_object_name = 'news'
    allow_empty = False
    paginate_by = 3

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'], is_published=True).select_related('category')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)  # чтоб не затереть предыдущее значение
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context


class ShowNews(DetailView):  # Кокретная новость
    model = News
    context_object_name = 'object'
    # pk_url_kwarg ='news_id'
    # template_name = 'news/show_news.html'


class CreateNews(CreateView):
    form_class = NewsForm
    template_name = 'news/add_news.html'
# success_url = reverse_lazy('home') #используется вместо get absolute url  в models

# def index(request):
#    news = News.objects.all()
#    context = {'news': news, 'title': "Новости", }
#    return render(request, 'news/index.html', context=context)


# def get_category(request, category_id):  # в базе создалась category_id
#    news = News.objects.filter(category_id=category_id)
#    categories = Category.objects.get(pk=category_id)
#    return render(request, 'news/category.html', {'news': news, 'categories': categories})


# def show_news(request, news_id):
#    try:
#        news_item = News.objects.get(pk=news_id)
#    except News.DoesNotExist:
#        raise Http404("Sorry, page not found :(")
#    return render(request, 'news/show_news.html', {'news_item': news_item})


# def add_news(request):
#    if request.method == 'POST':
#        form = NewsForm(request.POST)
#        if form.is_valid():
#            # new_news = News.objects.create(**form.cleaned_data) #для не связаной  формы
#            new_news = form.save()  # Сохраням в связаной форме
#            return redirect(new_news)
#    else:
#        form = NewsForm()
#    return render(request, 'news/add_news.html', {'form': form})
