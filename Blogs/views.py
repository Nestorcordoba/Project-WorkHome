from email import message
from django.shortcuts import render,redirect
from Blogs.forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def crear_post(request):
    if request.method == 'POST':
        form = FormularioPost(request.POST, request.FILES)
        if form.is_valid():
           post = form.save(commit=False)
           post.autor_id= request.user.id
           post.save()
           titulo= form.cleaned_data.get('titulo')
           messages.success(request, f'el post {titulo} se creo correctamente')
           return redirect('home')
        else:
            for mensaje in form.error_messages:
                messages.error(request, form.error_messages[mensaje])
            
    form= FormularioPost()       
    return render(request, 'Blogs/crear_post.html', {'form':form})

 