# Generated by Django 4.2.3 on 2023-07-13 20:41

from django.db import migrations, models
import django.db.models.deletion
import utils.model_validator


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SiteSetup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=65)),
                ('mostrar_cabecalho', models.BooleanField(default=True)),
                ('mostrar_pesquisa', models.BooleanField(default=True)),
                ('mostrar_menu', models.BooleanField(default=True)),
                ('mostrar_descricao', models.BooleanField(default=True)),
                ('mostrar_paginacao', models.BooleanField(default=True)),
                ('mostrar_rodape', models.BooleanField(default=True)),
                ('favicon', models.ImageField(blank=True, default='', upload_to='assets/favicon/%Y/%m/', validators=[utils.model_validator.validate_png])),
            ],
            options={
                'verbose_name': 'Setup',
                'verbose_name_plural': 'Setups',
            },
        ),
        migrations.CreateModel(
            name='MenuLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(max_length=50)),
                ('url', models.CharField(max_length=2048)),
                ('nova_aba', models.BooleanField(default=False)),
                ('site_setup', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='menu', to='site_setup.sitesetup')),
            ],
            options={
                'verbose_name': 'Menu Link',
                'verbose_name_plural': 'Menu Links',
            },
        ),
    ]