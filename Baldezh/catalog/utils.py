from django.core.mail import send_mail
from slugify import slugify

from Baldezh.settings import EMAIL_HOST_USER


def confirm(service):
    # send_mail(
    #     'Принятие объявления.',
    #     'Мы приняли ваше объявление, спасибо за то что пользуетесь нашим сервисом!',
    #     EMAIL_HOST_USER,
    #     [service.creator.email],
    #     fail_silently=False,
    # )
    service.slug = slugify(service.name)
    service.change_status_to_accepted()
    return True


def deny(service):
    send_mail(
        'Отказ объявления.',
        'Мы отклонили ваше объявление, ваше объявление не соответствовало правилам подачи услуг,спасибо за то что '
        'пользуетесь нашим сервисом!',
        EMAIL_HOST_USER,
        [service.creator.email],
        fail_silently=False,
    )
    service.change_status_to_accepted()
    return True
