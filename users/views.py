from django.shortcuts import render, redirect
from rest_framework import generics
from .models import StudData
from .serializer import UserSerializer
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from .forms import UserForm
from django.urls import reverse_lazy

class IndexView(ListView):
    template_name = 'users/index.html'
    context_object_name = 'all_users'

    def get_queryset(self):
        return StudData.objects.all()

class UserListCreate(generics.ListCreateAPIView):
    
    queryset = StudData.objects.all()
    serializer_class = UserSerializer

class UserRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = StudData.objects.all()
    serializer_class = UserSerializer

class StudDetail(DetailView): # inheriting from DetailView
    model = StudData
    template_name = 'users/detail.html'

class CollegeSearchView(ListView):
    template_name = 'users/index.html'
    context_object_name = 'all_users'
    model = StudData

    def get_queryset(self):
        query = self.request.GET.get('q')
        return StudData.objects.filter(college__icontains=query).order_by('-id')

def create(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('users:index')
    
    return render(request, 'users/item-form.html', {'form':form})


class UserUpdateView(UpdateView):
    model = StudData
    form_class = UserForm
    template_name = 'users/update-form.html'
    success_url = reverse_lazy('users:index')  

    def form_valid(self, form):
        user = form.save()
        return super().form_valid(form)
