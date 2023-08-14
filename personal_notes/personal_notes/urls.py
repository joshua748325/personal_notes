from django.contrib import admin
from django.urls import path, include
from note.views import SignupView, UserDetail, DeleteUser
# from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',TemplateView.as_view(template_name="note/index.html"),name='base'),
    path('signup/',SignupView.as_view(),name='signup'),
    path('user/delete/<int:pk>',DeleteUser.as_view(),name='delete'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('profile',UserDetail.as_view(),name='profile'),
    path('',include('note.urls')),
]

handler403='personal_notes.views.custom_403_view'
handler404='personal_notes.views.custom_404_view'
handler500='personal_notes.views.custom_500_view'