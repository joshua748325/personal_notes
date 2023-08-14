from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import View
from .models import Note
from .forms import SignupForm, NoteForm
from django.contrib.auth.mixins import LoginRequiredMixin

class SignupView(View):
    def get(self,request):
        form=SignupForm()
        return render(request,'registration/signup.html',{'form':form})
    def post(self,request):
        form=SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('login')+'?next='+reverse_lazy('note:home'))
        return render(request,'registration/signup.html',{'form':form})

class UserDetail(LoginRequiredMixin, View):
    def get(self,request):
        user=request.user
        return render(request,'note/profile.html',{'user':user})
    
class NoteList(LoginRequiredMixin, View):
    def get(self,request):
        notes=Note.objects.filter(created_by=request.user).order_by('-created_at')
        return render(request,'note/index.html',{'notes':notes})
    
class CreateNote(LoginRequiredMixin, View):
    def get(self,request):
        form=NoteForm()
        return render(request,'note/form.html',{'form':form,'button':'Create'})
    def post(self,request):
        form=NoteForm(request.POST)
        if form.is_valid():
            object=form.save(commit=False)
            object.created_by=request.user
            object.save()
            return redirect(reverse_lazy('note:home'))
        return render(request,'note/form.html',{'form':form,'button':'Create'})

class ReadNote(LoginRequiredMixin, View):
    def get(self,request,pk):
        note=get_object_or_404(Note, pk=pk)
        return render(request,'note/note.html',{'note':note})
    
class UpdateNote(LoginRequiredMixin, View):
    def get(self,request,pk):
        note=get_object_or_404(Note, pk=pk)
        form=NoteForm(instance=note)
        return render(request,'note/form.html',{'form':form,'button':'Update'})
    def post(self,request,pk):
        note=get_object_or_404(Note, pk=pk)
        form=NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('note:read_note',kwargs={'pk':note.id}))
        return render(request,'note/form.html',{'form':form,'button':'Update'})
    
class DeleteNote(View):
    def get(self,request,pk):
        note=get_object_or_404(Note,pk=pk)
        note.delete()
        return redirect(reverse_lazy('note:home'))
    
class StarNote(View):
    def get(self,request,pk):
        note=get_object_or_404(Note, pk=pk)
        note.is_starred= not note.is_starred
        note.save()
        url = request.GET['next']
        return redirect(url)

class StarNoteList(LoginRequiredMixin, View):
    def get(self,request):
        notes=Note.objects.filter(created_by=request.user).filter(is_starred=True)
        return render(request,'note/starred.html',{'notes':notes})