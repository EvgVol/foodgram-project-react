# Generated by Django 4.1.7 on 2023-03-04 05:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipes', '0002_alter_favorite_options_alter_ingredient_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ingredientinrecipe',
            options={'ordering': ('-id',), 'verbose_name': 'Количество ингредиента', 'verbose_name_plural': 'Количество ингредиентов'},
        ),
        migrations.AlterField(
            model_name='recipe',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Автор рецепта'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='tags',
            field=models.ManyToManyField(to='recipes.tag', verbose_name='Теги'),
        ),
    ]
