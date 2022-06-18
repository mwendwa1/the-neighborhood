from django.shortcuts import get_object_or_404, redirect, render
from hood.forms import BusinessForm, NeighborhoodForm, PostForm, SignUpForm, UpdateProfileForm
from django.contrib.auth import authenticate,login
from hood.models import Business, Neighborhood, Post, Profile
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user  = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form':form})


def hoods(request):
    all_hoods = Neighborhood.objects.all()
    all_hoods = all_hoods[::-1]
    context = {'all_hoods':all_hoods}
    return render(request, context, 'all_hoods.html')

def create_hood(request):
    if request.method == 'POST':
        form = NeighborhoodForm(request.POST, request.FILES)
        if form.is_valid():
            hood = form.save(commit=False)
            hood.save()
            return redirect('hood')
    else:
        form = NeighborhoodForm()
    return render(request, 'newhood.html', {'form':form})

def single_hood(request, hood_id):
    hood  = Neighborhood.objects.get(id=hood_id)
    business = Business.objects.filter(neighborhood=hood)
    posts = Post.objects.filter(hood=hood)
    posts = posts[::-1]
    if request.method == 'POST':
        form = BusinessForm(request.POST)
        if form.is_valid():
            b_form = form.save(commit=False)
            b_form = form.neighborhood = hood
            b_form.user = request.user.profile
            b_form.save()
            return redirect('single_hood', hood.id)
    else:
        form = BusinessForm()
    context = {
        'hood':hood,
        'business':business,
        'form':form,
        'posts':posts
    }
    return render(request, 'single_hood.html', context)

def hood_members(request, hood_id):
    hood = Neighborhood.objects.get(id=hood_id)
    members = Profile.objects.filter(neighborhood = hood)
    return render(request, 'members.html', {'members':members})

def create_post(request, hood_id):
    hood = Neighborhood.objects.get(id=hood_id)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.hood = hood
            post.user = request.user.profile
            post.save()
            return redirect('single_hood', hood.id)
    else:
        form = PostForm()
    return render(request, 'post.html', {'form':form})

def join_hood(request, id):
    neighborhood = get_object_or_404(Neighborhood, id=id)
    request.user.profile.neighborhood = neighborhood
    request.user.profile.save()
    return redirect('hood')

def leave_hood(request, id):
    neighborhood = get_object_or_404(Neighborhood, id=id)
    request.user.profile.neighborhood = None
    request.user.profile.save()
    return redirect('hood')

def profile(request, username):
    return render(request, 'profile.html')

def edit_profile(request, username):
    user = User.objects.get(username=username)
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile', user.username)
    else:
        form = UpdateProfileForm(instance=request.user.profile)
    return render(request, 'editprofile.html', {'form':form})

def search_business(request):
    if request.method == 'GET':
        name = request.GET.get('title')
        results = Business.objects.filter(name__icontains=name).all()
        message = f'name'
        context = {'results':results, 'message':message}
        return render(request, 'results.html', context)
    else:
        message = "You haven't searched for anything"
    return render(request, 'results.html')
