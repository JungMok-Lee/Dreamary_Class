from django.shortcuts import render, redirect, get_object_or_404
from .models import Designer

def home(request):
    designer=Designer.objects.all()
    return render(request,'home.html',{'designers' : designers})


def introduce(request):
    return render(request,'introduce.html')

def detail(request, designer_id):
    designer = get_object_or_404(Designer, pk=designer_id)
    return render(request,'detail.html',{'designer':designer})

def new(request):
    if request.method = 'POST':
        post = Designer()

def create(request):
    if request.method='POST':
        post=Designer()

        if 'image' in request.FILES:
            post.Image = request.FILES['image']
        post.name = request.POST['name']
        post.address = request.POST['address']
        post.descriptsion = request.POST['description']

        post.save()

        return redirect('detail', post.id)

def delete(request, designer_id):
    post=get_object_or_404(Designer, pk=designer_id)
    post.delete()

    return redirect('home')