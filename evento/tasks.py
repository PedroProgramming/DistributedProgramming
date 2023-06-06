from celery import shared_task
import os
from django.conf import settings
from .email import send_email
from PIL import Image, ImageDraw
from hashlib import sha256

@shared_task
def gerar_convite(name, email):
        path_template = os.path.join(settings.BASE_DIR, 'templates/static/img/convite.png')
        img = Image.open(path_template)
        img_escrever = ImageDraw.Draw(img)
        img_escrever.text((87, 189), name, fill=(0, 0, 0))
        key_secret = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ@&#$1234567890'
        token = sha256((email + key_secret).encode()).hexdigest()
        path_salvar = os.path.join(settings.BASE_DIR, f'media/convites/{token}.png')
        img.save(path_salvar)
        path_template = os.path.join(settings.BASE_DIR, 'evento/templates/email.html')
        send_email(path_template, 'Incrição realizado com sucesso!', [email,], nome=name, link=token)