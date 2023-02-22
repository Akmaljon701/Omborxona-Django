from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View
from .models import *

class LoginView(View):
    def get(self, request):
        return render(request, 'home.html')

    def post(self, request):
        user = authenticate(username=request.POST.get('l'),
                            password=request.POST.get('p'))

        if user is None:
            return redirect('/')
        login(request, user)
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
        soz = request.GET.get('q')
        if soz:
            data = {
                'clientlar': Client.objects.filter(ombor__user=request.user, ism__contains=soz) |
                             Client.objects.filter(ombor__user=request.user, nom__contains=soz) |
                             Client.objects.filter(ombor__user=request.user, manzil__contains=soz) |
                             Client.objects.filter(ombor__user=request.user, tel__contains=soz)
            }
            return render(request, 'clients.html', data)
        data = {
            'clientlar': Client.objects.filter(ombor__user=request.user)
        }
        return render(request, 'clients.html', data)
    def post(self, request):
        if request.user.is_authenticated:
            Client.objects.create(
                ism=request.POST.get('c_n'),
                nom=request.POST.get('c_sh'),
                tel=request.POST.get('c_p'),
                manzil=request.POST.get('c_a'),
                ombor=Ombor.objects.get(user=request.user)
            )
            return redirect('clientlar')

class ClientUpdateView(View):
    def get(self, request, pk):
        client = Client.objects.get(id=pk)
        if request.user.is_authenticated:
            data = {
                'client': client
            }
            return render(request, 'client_update.html', data)

    def post(self, request, pk):
        Client.objects.filter(id=pk).update(
            ism=request.POST.get('c_n'),
            tel=request.POST.get('c_p'),
        )
        return redirect('clientlar')
class ProductsView(View):
    def get(self, request):
        soz = request.GET.get('q')
        if soz:
            data = {
                'mahsulotlar':
                                Mahsulot.objects.filter(ombor__user=request.user, nom__contains=soz) |
                                Mahsulot.objects.filter(ombor__user=request.user, brend__contains=soz) |
                                Mahsulot.objects.filter(ombor__user=request.user, kelgan_sana__contains=soz)
            }
            return render(request, 'products.html', data)
        data = {
            'mahsulotlar': Mahsulot.objects.filter(ombor__user=request.user)
        }
        return render(request, 'products.html', data)

class ProductDelView(View):
    def get(self, request, pk):
        product = Mahsulot.objects.get(id=pk)
        if product.ombor == Ombor.objects.get(user=request.user):
            product.delete()
        return redirect('mahsulotlar')

class ProductUpdateView(View):
    def get(self, request, pk):
        product = Mahsulot.objects.get(id=pk)
        if product.ombor == Ombor.objects.get(user=request.user):
            data = {
                'product': product
            }
            return render(request, 'product_update.html', data)
        return redirect('mahsulotlar')

    def post(self, request, pk):
        Mahsulot.objects.filter(id=pk).update(
            narx=request.POST.get('price'),
            miqdor=request.POST.get('amount'),
        )
        return redirect('mahsulotlar')

class ClientDelView(View):
    def get(self, request, pk):
        client = Client.objects.get(id=pk)
        if client.ombor == Ombor.objects.get(user=request.user):
            client.delete()
        return redirect('clientlar')

