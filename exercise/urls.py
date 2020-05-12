from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from exercise import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('snippets/', views.snippet_list),
    path('snippets/<int:pk>/', views.snippet_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)