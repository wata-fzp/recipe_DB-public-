from django.views.generic import TemplateView

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.views.generic import CreateView, FormView
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.db.models import Q


from .forms import LoginForm, RecipeRegisterForm, SearchForm
from .models import Recipe
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

#############################################################################
class LoginView(TemplateView):
    template_name = "login.html"

    def post(self, request, *arg, **kwargs):
        form = LoginForm(data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            user     = User.objects.get(username=username)
            login(request, user)
            return redirect('/')
        return render(request, 'login.html', {'form': form,})
    
    def get(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        return render(request, 'login.html', {'form': form,})
    
    account_login = LoginView.as_view()

#############################################################################
class MenuView(TemplateView):
    template_name = "menu.html"
    
#############################################################################
class DisplayView(TemplateView):
    template_name = "display.html"
    
    def get(self, request, *args, **kwargs):
        context = super(DisplayView, self).get_context_data(**kwargs)
        menu_data = Recipe.objects.all()
        context['menu'] = menu_data
        
        return render(self.request, self.template_name, context)
    
    def index(request):
        menu_data = Recipe.objects.order_by('menu_id')
        paginator = Paginator(menu_data, 50)
        page = request.GET.get('page', 1)
        try:
            pages = paginator.page(page)
        except PageNotAnInteger:
            pages = paginator.page(1)
        except EmptyPage:
            pages = paginator.page(1)
        context = {'pages': pages}
        
        return render(request, 'display.html', context)

#############################################################################
class SearchView(TemplateView):
    template_name = "search.html"
    
    paginate_by = 20
    model = Recipe
    
    def post(self, request, *args, **kwargs):
        form_value = [
                self.request.POST.get('menu_id', None),
                self.request.POST.get('menu_name', None),
                self.request.POST.get('menu_category1', None),
                self.request.POST.get('menu_category2', None),
                self.request.POST.get('ingredient1', None),
                self.request.POST.get('ingredient2', None),
                self.request.POST.get('ingredient3', None),
                self.request.POST.get('ingredient4', None),
                self.request.POST.get('ingredient5', None),
                self.request.POST.get('ingredient6', None),
                self.request.POST.get('ingredient7', None),
                self.request.POST.get('ingredient8', None),
                self.request.POST.get('ingredient9', None),
                self.request.POST.get('ingredient10', None),
                self.request.POST.get('ingredient11', None),
                self.request.POST.get('ingredient12', None),
                self.request.POST.get('ingredient13', None),
                self.request.POST.get('ingredient14', None),
                self.request.POST.get('ingredient15', None),
                self.request.POST.get('ingredient16', None),
                self.request.POST.get('ingredient17', None),
                self.request.POST.get('ingredient18', None),
                self.request.POST.get('ingredient19', None),
                self.request.POST.get('ingredient20', None),
                self.request.POST.get('source', None),
                ]
        request.session['form_value'] = form_value
        
        self.request.GET = self.request.GET.copy()
        self.request.GET.clear()
        return self.get(request, *args, **kwargs)
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        menu_id = ''
        menu_name = ''
        menu_category1 = ''
        menu_category2 = ''
        ingredient1 = ''
        ingredient2 = ''
        ingredient3 = ''
        ingredient4 = ''
        ingredient5 = ''
        ingredient6 = ''
        ingredient7 = ''
        ingredient8 = ''
        ingredient9 = ''
        ingredient10 = ''
        ingredient11 = ''
        ingredient12 = ''
        ingredient13 = ''
        ingredient14 = ''
        ingredient15 = ''
        ingredient16 = ''
        ingredient17 = ''
        ingredient18 = ''
        ingredient19 = ''
        ingredient20 = ''
        source = ''
        
        
        if 'form_value' in self.request.session:
            form_value = self.request.session['form_value']
            menu_id = form_value[0]
            menu_name = form_value[1]
            menu_category1 = form_value[2]
            menu_category2 = form_value[3]
            ingredient1 = form_value[4]
            ingredient2 = form_value[5]
            ingredient3 = form_value[6]
            ingredient4 = form_value[7]
            ingredient5 = form_value[8]
            ingredient6 = form_value[9]
            ingredient7 = form_value[10]
            ingredient8 = form_value[11]
            ingredient9 = form_value[12]
            ingredient10 = form_value[13]
            ingredient11 = form_value[14]
            ingredient12 = form_value[15]
            ingredient13 = form_value[16]
            ingredient14 = form_value[17]
            ingredient15 = form_value[18]
            ingredient16 = form_value[19]
            ingredient17 = form_value[20]
            ingredient18 = form_value[21]
            ingredient19 = form_value[22]
            ingredient20 = form_value[23]
            source = form_value[24]
        
        default_data = {
                        'menu_id': menu_id,
                        'menu_name': menu_name,
                        'menu_category1': menu_category1,
                        'menu_category2': menu_category2,
                        'ingredient1': ingredient1,
                        'ingredient2': ingredient2,
                        'ingredient3': ingredient3,
                        'ingredient4': ingredient4,
                        'ingredient5': ingredient5,
                        'ingredient6': ingredient6,
                        'ingredient7': ingredient7,
                        'ingredient8': ingredient8,
                        'ingredient9': ingredient9,
                        'ingredient10': ingredient10,
                        'ingredient11': ingredient11,
                        'ingredient12': ingredient12,
                        'ingredient13': ingredient13,
                        'ingredient14': ingredient14,
                        'ingredient15': ingredient15,
                        'ingredient16': ingredient16,
                        'ingredient17': ingredient17,
                        'ingredient18': ingredient18,
                        'ingredient19': ingredient19,
                        'ingredient20': ingredient20,
                        'source': source,
                }
        text_form = SearchForm(initial=default_data)
        context['text_form'] = text_form
        return context
        
    def get_queryset(self):
        if 'form_value' in self.request.session:
            form_value = self.request.session['form_value']
            menu_id = form_value[0]
            menu_name = form_value[1]
            menu_category1 = form_value[2]
            menu_category2 = form_value[3]
            ingredient1 = form_value[4]
            ingredient2 = form_value[5]
            ingredient3 = form_value[6]
            ingredient4 = form_value[7]
            ingredient5 = form_value[8]
            ingredient6 = form_value[9]
            ingredient7 = form_value[10]
            ingredient8 = form_value[11]
            ingredient9 = form_value[12]
            ingredient10 = form_value[13]
            ingredient11 = form_value[14]
            ingredient12 = form_value[15]
            ingredient13 = form_value[16]
            ingredient14 = form_value[17]
            ingredient15 = form_value[18]
            ingredient16 = form_value[19]
            ingredient17 = form_value[20]
            ingredient18 = form_value[21]
            ingredient19 = form_value[22]
            ingredient20 = form_value[23]
            source = form_value[24]
            
            condition_menu_id = Q()
            condition_menu_name = Q()
            condition_menu_category1 = Q()
            condition_menu_category2 = Q()
            condition_ingredient1 = Q()
            condition_ingredient2 = Q()
            condition_ingredient3 = Q()
            condition_ingredient4 = Q()
            condition_ingredient5 = Q()
            condition_ingredient6 = Q()
            condition_ingredient7 = Q()
            condition_ingredient8 = Q()
            condition_ingredient9 = Q()
            condition_ingredient10 = Q()
            condition_ingredient11 = Q()
            condition_ingredient12 = Q()
            condition_ingredient13 = Q()
            condition_ingredient14 = Q()
            condition_ingredient15 = Q()
            condition_ingredient16 = Q()
            condition_ingredient17 = Q()
            condition_ingredient18 = Q()
            condition_ingredient19 = Q()
            condition_ingredient20 = Q()
            condition_source = Q()
            
            if len(menu_id) != 0 and menu_id[0]:
                condition_menu_id = Q(menu_id__contains=menu_id)
            if len(menu_name) != 0 and menu_name[1]:
                condition_menu_name = Q(menu_name__contains=menu_name)
            if len(menu_category1) != 0 and menu_category1[2]:
                condition_menu_category1 = Q(menu_category1__contains=menu_category1)
            if len(menu_category2) != 0 and menu_category2[3]:
                condition_menu_category2 = Q(menu_category2__contains=menu_category2)
            if len(ingredient1) != 0 and ingredient1[4]:
                condition_ingredient1 = Q(ingredient1__contains=ingredient1)
            if len(ingredient2) != 0 and ingredient2[5]:
                condition_ingredient2 = Q(ingredient2__contains=ingredient2)
            if len(ingredient3) != 0 and ingredient3[6]:
                condition_ingredient3 = Q(ingredient3__contains=ingredient3)
            if len(ingredient4) != 0 and ingredient4[7]:
                condition_ingredient4 = Q(ingredient4__contains=ingredient4)
            if len(ingredient5) != 0 and ingredient5[8]:
                condition_ingredient5 = Q(ingredient5__contains=ingredient5)
            if len(ingredient6) != 0 and ingredient6[9]:
                condition_ingredient6 = Q(ingredient6__contains=ingredient6)
            if len(ingredient7) != 0 and ingredient7[10]:
                condition_ingredient7 = Q(ingredient7__contains=ingredient7)
            if len(ingredient8) != 0 and ingredient8[11]:
                condition_ingredient8 = Q(ingredient8__contains=ingredient8)
            if len(ingredient9) != 0 and ingredient9[12]:
                condition_ingredient9 = Q(ingredient9__contains=ingredient9)
            if len(ingredient10) != 0 and ingredient10[13]:
                condition_ingredient10 = Q(ingredient10__contains=ingredient10)
            if len(ingredient11) != 0 and ingredient11[14]:
                condition_ingredient11 = Q(ingredient11__contains=ingredient11)
            if len(ingredient12) != 0 and ingredient12[15]:
                condition_ingredient12 = Q(ingredient12__contains=ingredient12)
            if len(ingredient13) != 0 and ingredient13[16]:
                condition_ingredient13 = Q(ingredient13__contains=ingredient13)
            if len(ingredient14) != 0 and ingredient14[17]:
                condition_ingredient14 = Q(ingredient14__contains=ingredient14)
            if len(ingredient15) != 0 and ingredient15[18]:
                condition_ingredient15 = Q(ingredient15__contains=ingredient15)
            if len(ingredient16) != 0 and ingredient16[19]:
                condition_ingredient16 = Q(ingredient16__contains=ingredient16)
            if len(ingredient17) != 0 and ingredient17[20]:
                condition_ingredient17 = Q(ingredient17__contains=ingredient17)
            if len(ingredient18) != 0 and ingredient18[21]:
                condition_ingredient18 = Q(ingredient18__contains=ingredient18)
            if len(ingredient19) != 0 and ingredient19[22]:
                condition_ingredient19 = Q(ingredient19__contains=ingredient19)
            if len(ingredient20) != 0 and ingredient20[23]:
                condition_ingredient20 = Q(ingredient20__contains=ingredient20)
            if len(source) != 0 and source[24]:
                condition_source = Q(source__contains=source)
                
                
            return Recipe.objects.select_related().filter(condition_menu_id & condition_menu_name &
                                                condition_menu_category1 & condition_menu_category2 &
                                                condition_ingredient1 & condition_ingredient2 &
                                                condition_ingredient1 & condition_ingredient2 &
                                                condition_ingredient3 & condition_ingredient4 &
                                                condition_ingredient5 & condition_ingredient6 &
                                                condition_ingredient7 & condition_ingredient8 &
                                                condition_ingredient9 & condition_ingredient10 &
                                                condition_ingredient11 & condition_ingredient12 &
                                                condition_ingredient13 & condition_ingredient14 &
                                                condition_ingredient15 & condition_ingredient16 &
                                                condition_ingredient17 & condition_ingredient18 &
                                                condition_ingredient19 & condition_ingredient20 &
                                                condition_source                                                    
                                                )
        else:
            return Recipe.objects.none()
        
#############################################################################   
class RegisterView(TemplateView):
    template_name = "register.html"
    form_class = RecipeRegisterForm
    success_url = '/'
    
    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.SUCCESS, 'registered!!')

        return super().form_valid(form)
                
#############################################################################    
class RecordView(TemplateView):
    template_name = "record.html"
    
#############################################################################    
class LogoutView(TemplateView):
    template_name = "login.html"
    