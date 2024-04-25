from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, logout, update_session_auth_hash
from .forms import RegistrationForm, UserProfileForm, ChangePasswordForm
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth import authenticate, login
#найди пару
from django.shortcuts import render, redirect
from .forms import FindPairTaskForm, PairElementForm
from django.contrib.auth.decorators import login_required
from study_buddy.models import FindPairTask


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            group_name = request.POST.get('group')  
            
            try:
                group = Group.objects.get(name=group_name)  
            except Group.DoesNotExist:

                return render(request, 'registration.html', {'form': form, 'error_message': 'Выбранная группа не найдена'})

            user = form.save()

            user.groups.add(group)

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')  
            else:
                return render(request, 'registration.html', {'form': form, 'error_message': 'Не удалось войти в систему после регистрации'})
    else:
        form = UserCreationForm()
    return render(request, 'registration.html', {'form': form})



def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')  
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def profile_view(request):
    user = request.user
    user_role = user.groups.first()  
    return render(request, 'profile.html', {'user': user, 'user_role': user_role})


def logout_view(request):
    logout(request)  
    return redirect('index')  

def index(request):
    return render(request, 'index.html')


@login_required
def edit_profile(request):
    if request.method == 'POST':
        user_form = UserProfileForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            return redirect('profile')
    else:
        user_form = UserProfileForm(instance=request.user)
    return render(request, 'edit_profile.html', {'user_form': user_form})

@login_required
def change_password(request):
    if request.method == 'POST':
        password_form = ChangePasswordForm(request.POST)
        if password_form.is_valid():
            old_password = password_form.cleaned_data['old_password']
            new_password = password_form.cleaned_data['new_password1']
            if request.user.check_password(old_password):
                request.user.set_password(new_password)
                request.user.save()
                return redirect('profile')
            else:
                password_form.add_error('old_password', 'Неверный пароль')
    else:
        password_form = ChangePasswordForm()
    return render(request, 'change_password.html', {'form': password_form})  


def change_password_view(request):
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            old_password = form.cleaned_data['old_password']
            new_password = form.cleaned_data['new_password1']
            if request.user.check_password(old_password):
                request.user.set_password(new_password)
                request.user.save()
                return redirect('profile')
            else:
                form.add_error('old_password', 'Неверный пароль')
    else:
        form = ChangePasswordForm()
    return render(request, 'change_password.html', {'form': form})


def task_creation(request):
    return render(request, 'task_creation.html')

def find_pair_task_creation(request):
    return render(request, 'find_pair_task_creation.html')

def fill_blanks_task_creation(request):
    return render(request, 'fill_blanks_task_creation.html')

def pair_creation(request):
    return render(request, 'pair_creation.html')


@login_required
def create_find_pair_task(request):
    if request.method == 'POST':
        task_form = FindPairTaskForm(request.POST)
        pair_form = PairElementForm(request.POST)
        if task_form.is_valid() and pair_form.is_valid():
            task = task_form.save(commit=False)
            task.author = request.user
            task.save()
            pair = pair_form.save(commit=False)
            pair.task = task
            pair.save()
            return redirect('preview_find_pair_task', task_id=task.pk)
    else:
        task_form = FindPairTaskForm()
        pair_form = PairElementForm()
    return render(request, 'find_pair_task_creation.html', {'task_form': task_form, 'pair_form': pair_form})

@login_required
def preview_find_pair_task(request, task_id):
    task = FindPairTask.objects.get(pk=task_id)
    pairs = task.pairs.all()
    return render(request, 'preview_find_pair_task.html', {'task': task, 'pairs': pairs})

