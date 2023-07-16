from django.db import models
from utils.model_validator import validate_png
from utils.images import resize_image

class MenuLink(models.Model):
    class Meta:
        verbose_name = 'Menu Link'
        verbose_name_plural = 'Menu Links'

    texto = models.CharField(max_length=50)
    url = models.CharField(max_length=2048)
    nova_aba = models.BooleanField(default=False)
    site_setup = models.ForeignKey(
        'SiteSetup',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        default=None,
        related_name='menu',
    )

    def __str__(self):
        return self.texto

class SiteSetup(models.Model):
    class Meta:
        verbose_name = 'Setup'
        verbose_name_plural = 'Setups'

    titulo = models.CharField(max_length=65)
    mostrar_cabecalho = models.BooleanField(default=True)
    mostrar_pesquisa = models.BooleanField(default=True)
    mostrar_menu = models.BooleanField(default=True)
    mostrar_descricao = models.BooleanField(default=True)
    mostrar_paginacao = models.BooleanField(default=True)
    mostrar_rodape = models.BooleanField(default=True)
    favicon = models.ImageField(
        upload_to='assets/favicon/%Y/%m/',
        blank=True,
        default='',
        validators=[validate_png],    
    )


    def save(self, *args, **kwargs):
        current_favicon_name = str(self.favicon.name)
        super().save(*args, **kwargs)
        favicon_changed = False

        if self.favicon:
            favicon_changed = current_favicon_name != self.favicon.name

        if favicon_changed:
            resize_image(self.favicon, 32)

    def __str__(self):
        return self.titulo