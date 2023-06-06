from django.shortcuts import render
from .models import InscricaoEvento
from .tasks import gerar_convite

def incricao(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    
    user_incricao = InscricaoEvento.objects.create(
        name=name,
        email=email
    )
    user_incricao.save()
    gerar_convite.delay(name, email)
    return render(request, 'inscricao.html')


def test(request):
    return render(request, 'test.html')
    