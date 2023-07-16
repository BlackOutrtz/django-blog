from django.db import models
from utils.rands import slugify_new
from utils.images import resize_image
from blog.models import Category


class Mundo(models.Model):
    class Meta:
        verbose_name = 'Mundo'
        verbose_name_plural = 'Mundo'

    title = models.CharField(max_length=65)
    slug = models.SlugField(
        unique=True, default="",
        null=False, blank=True, max_length=255
    )
    excerpt = models.CharField(max_length=150)
    is_published = models.BooleanField(
        default=False,
        help_text=(
            'Este campo precisara estar marcado',
            'para a pagina ser exibida publicamente.',
        ),
    )
    content = models.TextField()
    cover = models.ImageField(upload_to='posts/%Y/%m/', blank=True, default='')
    cover_in_post_content = models.BooleanField(
        default=True,
        help_text=(
            'Se marcado, exibirá a capa dentro do post.',    
        )
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True,
        blank=True, default=None,  
    )


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify_new(self.title, 4)
        
        current_cover_name = str(self.cover.name)
        super_save = super().save(*args, **kwargs)
        cover_changed = False

        if self.cover:
            cover_changed = current_cover_name != self.cover.name

        if cover_changed:
            resize_image(self.cover, 900, True, 70)

        return super_save

    def __str__(self) -> str:
        return self.title


class Politica(models.Model):
    class Meta:
        verbose_name = 'Política'
        verbose_name_plural = 'Política'

    title = models.CharField(max_length=65)
    slug = models.SlugField(
        unique=True, default="",
        null=False, blank=True, max_length=255
    )
    excerpt = models.CharField(max_length=150)
    is_published = models.BooleanField(
        default=False,
        help_text=(
            'Este campo precisara estar marcado',
            'para a pagina ser exibida publicamente.',
        ),
    )
    content = models.TextField()
    cover = models.ImageField(upload_to='posts/%Y/%m/', blank=True, default='')
    cover_in_post_content = models.BooleanField(
        default=True,
        help_text=(
            'Se marcado, exibirá a capa dentro do post.',    
        )
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True,
        blank=True, default=None,  
    )


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify_new(self.title, 4)
        
        current_cover_name = str(self.cover.name)
        super_save = super().save(*args, **kwargs)
        cover_changed = False

        if self.cover:
            cover_changed = current_cover_name != self.cover.name

        if cover_changed:
            resize_image(self.cover, 900, True, 70)

        return super_save

    def __str__(self) -> str:
        return self.title
    

class PopArtes(models.Model):
    class Meta:
        verbose_name = 'PopArte'
        verbose_name_plural = 'PopArte'

    title = models.CharField(max_length=65)
    slug = models.SlugField(
        unique=True, default="",
        null=False, blank=True, max_length=255
    )
    excerpt = models.CharField(max_length=150)
    is_published = models.BooleanField(
        default=False,
        help_text=(
            'Este campo precisara estar marcado',
            'para a pagina ser exibida publicamente.',
        ),
    )
    content = models.TextField()
    cover = models.ImageField(upload_to='posts/%Y/%m/', blank=True, default='')
    cover_in_post_content = models.BooleanField(
        default=True,
        help_text=(
            'Se marcado, exibirá a capa dentro do post.',    
        )
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True,
        blank=True, default=None,  
    )


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify_new(self.title, 4)
        
        current_cover_name = str(self.cover.name)
        super_save = super().save(*args, **kwargs)
        cover_changed = False

        if self.cover:
            cover_changed = current_cover_name != self.cover.name

        if cover_changed:
            resize_image(self.cover, 900, True, 70)

        return super_save

    def __str__(self) -> str:
        return self.title
    
class Economia(models.Model):
    class Meta:
        verbose_name = 'Economia'
        verbose_name_plural = 'Economia'

    title = models.CharField(max_length=65)
    slug = models.SlugField(
        unique=True, default="",
        null=False, blank=True, max_length=255
    )
    excerpt = models.CharField(max_length=150)
    is_published = models.BooleanField(
        default=False,
        help_text=(
            'Este campo precisara estar marcado',
            'para a pagina ser exibida publicamente.',
        ),
    )
    content = models.TextField()
    cover = models.ImageField(upload_to='posts/%Y/%m/', blank=True, default='')
    cover_in_post_content = models.BooleanField(
        default=True,
        help_text=(
            'Se marcado, exibirá a capa dentro do post.',    
        )
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True,
        blank=True, default=None,  
    )


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify_new(self.title, 4)
        
        current_cover_name = str(self.cover.name)
        super_save = super().save(*args, **kwargs)
        cover_changed = False

        if self.cover:
            cover_changed = current_cover_name != self.cover.name

        if cover_changed:
            resize_image(self.cover, 900, True, 70)

        return super_save

    def __str__(self) -> str:
        return self.title
    

class Tecnologia(models.Model):
    class Meta:
        verbose_name = 'Tecnologia'
        verbose_name_plural = 'Tecnologia'

    title = models.CharField(max_length=65)
    slug = models.SlugField(
        unique=True, default="",
        null=False, blank=True, max_length=255
    )
    excerpt = models.CharField(max_length=150)
    is_published = models.BooleanField(
        default=False,
        help_text=(
            'Este campo precisara estar marcado',
            'para a pagina ser exibida publicamente.',
        ),
    )
    content = models.TextField()
    cover = models.ImageField(upload_to='posts/%Y/%m/', blank=True, default='')
    cover_in_post_content = models.BooleanField(
        default=True,
        help_text=(
            'Se marcado, exibirá a capa dentro do post.',    
        )
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True,
        blank=True, default=None,  
    )


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify_new(self.title, 4)
        
        current_cover_name = str(self.cover.name)
        super_save = super().save(*args, **kwargs)
        cover_changed = False

        if self.cover:
            cover_changed = current_cover_name != self.cover.name

        if cover_changed:
            resize_image(self.cover, 900, True, 70)

        return super_save

    def __str__(self) -> str:
        return self.title
    

class Educacao(models.Model):
    class Meta:
        verbose_name = 'Educação'
        verbose_name_plural = 'Educação'

    title = models.CharField(max_length=65)
    slug = models.SlugField(
        unique=True, default="",
        null=False, blank=True, max_length=255
    )
    excerpt = models.CharField(max_length=150)
    is_published = models.BooleanField(
        default=False,
        help_text=(
            'Este campo precisara estar marcado',
            'para a pagina ser exibida publicamente.',
        ),
    )
    content = models.TextField()
    cover = models.ImageField(upload_to='posts/%Y/%m/', blank=True, default='')
    cover_in_post_content = models.BooleanField(
        default=True,
        help_text=(
            'Se marcado, exibirá a capa dentro do post.',    
        )
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True,
        blank=True, default=None,  
    )


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify_new(self.title, 4)
        
        current_cover_name = str(self.cover.name)
        super_save = super().save(*args, **kwargs)
        cover_changed = False

        if self.cover:
            cover_changed = current_cover_name != self.cover.name

        if cover_changed:
            resize_image(self.cover, 900, True, 70)

        return super_save

    def __str__(self) -> str:
        return self.title
    

class Saude(models.Model):
    class Meta:
        verbose_name = 'Saude'
        verbose_name_plural = 'Saude'

    title = models.CharField(max_length=65)
    slug = models.SlugField(
        unique=True, default="",
        null=False, blank=True, max_length=255
    )
    excerpt = models.CharField(max_length=150)
    is_published = models.BooleanField(
        default=False,
        help_text=(
            'Este campo precisara estar marcado',
            'para a pagina ser exibida publicamente.',
        ),
    )
    content = models.TextField()
    cover = models.ImageField(upload_to='posts/%Y/%m/', blank=True, default='')
    cover_in_post_content = models.BooleanField(
        default=True,
        help_text=(
            'Se marcado, exibirá a capa dentro do post.',    
        )
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True,
        blank=True, default=None,  
    )


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify_new(self.title, 4)
        
        current_cover_name = str(self.cover.name)
        super_save = super().save(*args, **kwargs)
        cover_changed = False

        if self.cover:
            cover_changed = current_cover_name != self.cover.name

        if cover_changed:
            resize_image(self.cover, 900, True, 70)

        return super_save

    def __str__(self) -> str:
        return self.title