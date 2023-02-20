from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View


class LoginView(View):
    def get(self, request):
        return render(request, 'home.html')

    def post(self, request):
        user = authenticate(username=request.POST.get('l'),
                            password=request.POST.get('p'))

        if user is None:
            return redirect('/')
        login(user, request)
        return redirect('/bolim/')

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("/")

class BolimView(View):
    def get(self, request):
        return render(request, 'bulimlar.html')

class StatsView(View):
    def get(self, request):
        return render(request, 'stats.html')

class ClientsView(View):
    def get(self, request):
        return render(request, 'clients.html')

class ProductsView(View):
    def get(self, request):
        return render(request, 'products.html')

class Client_updateView(View):
    def get(self, request):
        return render(request, 'client_update.html')

class Product_updateView(View):
    def get(self, request):
        return render(request, 'product_update.html')