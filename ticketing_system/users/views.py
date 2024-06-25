from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .form import RegisterCustomerForm, LoginForm




def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            # print(user.password, "fghjk")
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                form.add_error(None, "Invalid username or password")
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})

def register_customer(request):
    if request.method == 'POST':
        form = RegisterCustomerForm(request.POST)
        if form.is_valid():
            user = form.save() 
            print(user) # Create the user object but don't save to the database yet
            user.set_password(form.cleaned_data['password1'])  # Hash the password
            user.save()  # Save the user with the hashed password
            return redirect('login')
    else:
        form = RegisterCustomerForm()
    return render(request, 'users/register-customer.html', {'form': form})

# def register_customer(request):
#      if request.method == 'POST':
#         form = RegisterCustomerForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#      else:
#         form = RegisterCustomerForm()
#      return render(request, 'users/register-customer.html', {'form': form})


    # if request.method == 'POST':
    #     form = RegisterCustomerForm(request.POST)
    #     if form.is_valid():
    #         var= form.save(commit=False)
    #         print(var, "varrrrr") # we don't want it to save in database.
    #         var.is_customer = True
    #         var.save()
    #         print(var)
    #         messages.info(request, "Your account has been successfully registered. Please Login")
    #         return redirect('login')
    #     else:
    #         print(form.errors)
    #         messages.warning(request,'Something went Wrong.')
    #         return redirect('register-customer')
        
    # else:
    #     form = RegisterCustomerForm()
    #     context ={'form' : form}
    #     return render(request, 'users/register-customer.html', context)


# def login_user(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(request, username=username, password=password)
#             print(user)
#             if user:
#                 login(request, user)        
#                 return redirect('dashboard')
#     else:
#         form = LoginForm()
#     return render(request, 'users/login.html', {'form': form})

    # if request.method == 'POST':
    #     username = request.POST.get('username')
    #     password = request.POST.get('password')
    #     print(username, password)

    #     print(f"Attempting to login with username: {username}")


    #     user = authenticate(request, username= username, password=password)
    #     print(user)
    #     if user is not None:
    #         print(f"User is_active: {user.is_active}")
    #         if user.is_active:
    #             login(request, user)
    #             messages.info(request, 'Login Successful !!')
    #             return redirect('dashboard')
    #         else:
    #             messages.warning(request, 'User account is not active.')
    #             return redirect('login')
    #     else:
    #         messages.warning(request, 'Invalid username or password.')
    #         return redirect('login')
    # else:
    #     return render(request, 'users/login.html')
    

def logout_user(request):
    logout(request)
    messages.info(request, 'Your session has ended')
    return redirect('login')
    


        






