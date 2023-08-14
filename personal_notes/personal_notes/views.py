from django.shortcuts import render

def custom_403_view(request, exception):
    return render(request,'note/403.html')

def custom_404_view(request, exception):
    return render(request,'note/404.html')

def custom_500_view(request):
    return render(request,'note/500.html')