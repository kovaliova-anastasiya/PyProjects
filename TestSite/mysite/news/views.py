from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView  # предназначен для работы со списками
from .models import News, Category
from .forms import NewsForm, UserRegisterForm, UserLoginForm
from django.urls import reverse_lazy
from .utils import MyMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth import login, logout


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)  # форма, связанная с данными (моделью)
        # проводим валидацию формы
        if form.is_valid():
            # сразу же авторизуем юзера с пом. встроенной ф-ции login()
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('home')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()  # форма, не связаная с данными
    return render(request, 'news/register.html', {'form': form})

def user_login(request):
    # if request is not post, initialize an empty form
    form = UserLoginForm()
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)  # форма не хочет работать из-за data=request.POST!!!
        if form.is_valid():
            user = form.get_user()
            # login - это встроенная функция
            login(request, user)
            return redirect('home')

    return render(request, 'news/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')


def test(request):
    objects = ['john1', 'paul2', 'george3', 'ringo4', 'john5', 'paul6', 'george7']
    paginator = Paginator(objects, 2)
    page_num = request.GET.get('page', 1)
    page_objects = paginator.get_page(page_num)
    return render(request, 'news/test.html', {'page_obj': page_objects})


class HomeNews(ListView, MyMixin):
    model = News  # буквально аналог строки news = News.objects.all()
    # будут получены все данные из News
    # тк появился класс, изменили маршрут в urls! там же функция index вызывается
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    # extra_context = {'title': 'Главная'}  # этот атрибут желательно использовать для статичных данных
    # для динамичных данных, те для списков его использовать не рекомендуется
    # для этого есть метод, который надо переопределить
    mixin_prop = ''
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.get_upper('Главная страница')
        context['mixin_prop'] = self.get_prop()
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True).select_related('category')


class NewsByCategory(ListView, MyMixin):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    allow_empty = False
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.get_upper(Category.objects.get(pk=self.kwargs['category_id']))
        # get получение данных текущей категории
        return context

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'], is_published=True).select_related('category')


class ViewNews(DetailView):
    model = News
    # pk_url_kwarg = 'news_id'
    # template_name = 'news/news_detail.html'
    context_object_name = 'news_item'


class CreateNews(LoginRequiredMixin, CreateView):
    form_class = NewsForm
    template_name = 'news/add_news.html'
    # всё будет работать, тк в модели есть метод get_absolute_url
    # success_url = reverse_lazy('home')
    login_url = '/admin/'
    raise_exception = True


# def index(request):
#     # print(dir(request))
#     news = News.objects.all()
#     context = {
#         'news': news,
#         'title': 'Список новостей',
#     }
#
#     return render(request, template_name='news/index.html', context=context)


# def get_category(request, category_id):
#     news = News.objects.filter(category_id=category_id)
#     category = Category.objects.get(pk=category_id)
#     return render(request, 'news/category.html', {'news': news, 'category': category})


# def view_news(request, news_id):
#     # news_item = News.objects.get(pk=news_id)
#     news_item = get_object_or_404(News, pk=news_id)
#     return render(request, 'news/view_news.html', {'news_item': news_item})



# def add_news(request):
#     if request.method == 'POST':
#         form = NewsForm(request.POST)
#         if form.is_valid():
#             # print(form.cleaned_data)
#             # news = News.objects.create(**form.cleaned_data)  # возвращает объект созданной записи
#             news = form.save()
#             return redirect(news)
#     else:
#         form = NewsForm
#     return render(request, 'news/add_news.html', {'form': form})


