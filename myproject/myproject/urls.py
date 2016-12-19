"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from ex_design_template import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^demo/$',views.index),
    # url(r'^demo/detail123/([0-9])/$',views.detail), #{4}: gioi han so ki tu
    url(r'^design/$',views.ListTemplateView.as_view()),
    url(r'^design/detailTemplate/([0-9]+)/$',views.DetailTemplateView.as_view()),
    url(r'^design/new/$',views.PostTemplateView.as_view()),
    url(r'^design/edit/([0-9]+)/$',views.EditTemplateView.as_view()),
    url(r'^design/delete/([0-9]+)/$',views.DeleteTemplateView.as_view())
]

#^:bat dau
#$:ket thuc
