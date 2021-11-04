from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from .views import LoginView, MenuView, DisplayView, SearchView, RecordView, RegisterView, LogoutView

urlpatterns = [
    #url(r'^recipe_site/', include('recipe_site.urls')),
    path('', LoginView.as_view(), name='login'),
    path('menu/', MenuView.as_view(), name='menu'),
    path('display/', DisplayView.as_view(), name='display'),
    path('search/', SearchView.as_view(), name='search'),
    path('record/', RecordView.as_view(), name='record'),
    path('register/', RegisterView.as_view(), name='register'),
    path('', LogoutView.as_view(), name='logout'),
    #admin
    path('admin/', admin.site.urls),
]

"""
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
"""