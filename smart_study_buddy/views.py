from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, logout, update_session_auth_hash, authenticate
from .forms import RegistrationForm, UserProfileForm, ChangePasswordForm
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from study_buddy.models import Task, Pair
from django.contrib import messages
from django.http import JsonResponse


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

def create_find_pair_task(request):
    if request.method == 'POST':
        task_title = request.POST['task_title']
        task_description = request.POST['task_description']
        task = Task.objects.create(title=task_title, description=task_description)

        saved_pairs = set()  
        for key, value in request.POST.items():
            if key.startswith('pair_'):
                pair_num = key.split('_')[1]
                first_text = request.POST.get(f'pair_{pair_num}_first_text')
                first_image = request.FILES.get(f'pair_{pair_num}_first_image')
                second_text = request.POST.get(f'pair_{pair_num}_second_text')
                second_image = request.FILES.get(f'pair_{pair_num}_second_image')

                if (first_text, first_image, second_text, second_image) not in saved_pairs:
                    Pair.objects.create(
                        task=task,
                        first_element_text=first_text,
                        first_element_image=first_image,
                        second_element_text=second_text,
                        second_element_image=second_image
                    )
                    saved_pairs.add((first_text, first_image, second_text, second_image))

        messages.success(request, 'Задание успешно создано!')
        return redirect(reverse_lazy('task_creation'))  

    return render(request, 'create_find_pair_task.html')

def task_view(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    pairs = task.pair_set.all()  
    return render(request, 'task.html', {'task': task, 'pairs': pairs})

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})