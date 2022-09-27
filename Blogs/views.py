from email import message
from django.shortcuts import render,redirect
from Blogs.forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from Blogs.models import *
from django.core.paginator import Paginator
# Create your views here.

@login_required(login_url='/AppLogin/login/')
def posteos(request):
    listado_posts = Post.objects.all()
    paginator = Paginator(listado_posts, 3)
    pagina = request.GET.get("page") or 1
    posts = paginator.get_page(pagina)
    pagina_actual = int(pagina)
    paginas = range(1, posts.paginator.num_pages + 1)
    return render(request, "Blogs/posteos.html", {'posts': posts, "paginas": paginas, "pagina_actual":pagina_actual})




@login_required(login_url='/AppLogin/login/')
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

 