from email import message
from django.shortcuts import render,redirect
from Blogs.forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from Blogs.models import *
from django.core.paginator import Paginator
from django.views.generic import UpdateView
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


'''@login_required(login_url='/AppLogin/login/')
def eliminar_post(request, post_id):
    try:
        post = Post.objects.get(pk = post_id)
    except Post.DoesNotExist:
        messages.error(request, "el post que quieres eliminar no existe")
        return redirect("posteos")

    if post.autor != request.user:
        messages.error(request, "no eres el autor de este post")
        return redirect("posteos")

    post.delete()
    messages.error(request, f"el post {post.titulo} ha sido eliminado")
    return redirect("posteos")'''
@login_required(login_url='/AppLogin/login/')
def eliminar_post(request, post_id):
    post=Post.objects.get(id=post_id)
    post.delete()
    posts=Post.objects.all()
    return render(request, "Blogs/posteos.html", {"posts":posts})

@login_required(login_url='/AppLogin/login/')
def editar_post(request, id):
    #traer el post
    post=Post.objects.get(id=id)
    if request.method=="POST":
        #el form viene lleno, con los datos a cambiar
        form=FormularioPost(request.POST)
        if form.is_valid():
            #cambio los datos
            info=form.cleaned_data
            post.titulo=info["titulo"]
            post.subtitulo=info["subtitulo"]
            post.contenido=info["contenido"]
            #guardo el post
            post.save()
            #vuelvo a la vista del listado para ver el cambio
           #posteos=Post.objects.all()
           # return render(request, "Blogs/posteos.html", {"posteos":posteos})
            return redirect('posteos')
    else:
        form= FormularioPost(initial={"titulo": post.titulo, "subtitulo": post.subtitulo, "contenido": post.contenido})
        return render(request, "Blogs/editarPost.html", {"formulario":form, "titulo":post.titulo, "id":post.id})


def detalle_post(request, id):
    post= Post.objects.get(id = id)
    return render(request, "Blogs/ver_post.html", {"post":post})