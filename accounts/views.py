 
from django.shortcuts import render, redirect
from django.http import HttpResponse
#from django.forms import inlineforset_factory
from django.forms.formsets import formset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout

from .forms import CreateUserForm

from django.contrib.auth.decorators import login_required


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('listings')

    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'account was created for' + user)
                
                #when register redirect to login
                return redirect('login')

    context = {'form': form}
    return render(request, 'accounts/register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
         return redirect('listings')

    else:

        if request.method == 'POST':
            username=request.POST.get('username')
            password=request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                #redirect home
                return redirect('listings')

            else:
                messages.info(request, 'username or pasword is incorrect')
                #return render(request, 'accounts/login.html', context)


        # form = UserCreationForm()
        context = {}
        return render(request, 'accounts/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')






# from rest_framework import generics, permissions
# from rest_framework.response import Response
# from knox.models import AuthToken
# from .serializers import UserSerializer, RegisterSerializer

# # Register API
# class RegisterAPI(generics.GenericAPIView):
#     serializer_class = RegisterSerializer

#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.save()
#         return Response({
#         "user": UserSerializer(user, context=self.get_serializer_context()).data,
#         "token": AuthToken.objects.create(user)[1]
#         })