from django.contrib import admin
from django.urls import path, include
from note.views import SignupView, UserDetail
# from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',TemplateView.as_view(template_name="note/index.html"),name='base'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('signup/',SignupView.as_view(),name='signup'),
    path('profile',UserDetail.as_view(),name='profile'),
    path('',include('note.urls')),
]
