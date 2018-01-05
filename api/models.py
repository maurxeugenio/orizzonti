from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

class Contact(models.Model):
    name = models.CharField(_('nome completo'), max_length=40)
    subject = models.CharField(_('assunto'), max_length=40)
    email = models.EmailField(_('e-mail'))
    message = models.TextField(_('menssgem'), max_length=300)
    create_date = models.DateTimeField(_('enviado em:'), default=timezone.now)

    def __str__(self):
        return 'Assunto: {} de {}'.format(self.subject, self.name)

    class Meta:
        verbose_name = 'contato'
        verbose_name_plural = 'contatos'
