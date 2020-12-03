from django.contrib import admin
from django.urls import path, include
from question.views import question_list_view
import debug_toolbar
urlpatterns = [
    path('', question_list_view, name='question_list_view'),
    path('admin/', admin.site.urls),
    path('answers/', include('answer.urls')),
    path('question/', include('question.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('account.urls')),



]
