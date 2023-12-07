"""
URL configuration for query project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.views import query_examples,questao01,questao02,questao03,questao04,questao05,questao06,questao07,questao08,questao09,questao10

urlpatterns = [
    path('admin/', admin.site.urls),
    path('teste1/',query_examples),
    path('questao1/',questao01),
    path('questao2/',questao02),
    path('questao3/',questao03),
    path('questao4/',questao04),
    path('questao5/',questao05),
    path('questao6/',questao06),
    path('questao7/',questao07),
    path('questao8/',questao08),
    path('questao9/',questao09),
    path('questao10/',questao10),
]
