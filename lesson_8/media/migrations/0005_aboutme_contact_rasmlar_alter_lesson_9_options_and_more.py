# Generated by Django 4.2.7 on 2023-11-20 19:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0004_alter_lesson_9_icon_alter_mediauser_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aboutme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Ism')),
                ('about', models.TextField(default='Men Grafik dizaynerman', verbose_name='Men haqimda qisqacha')),
                ('my_app', models.TextField(blank=True, verbose_name='Men ishlaydigan dasturlar')),
                ('my_persent', models.CharField(default=50, verbose_name='Qay darajada bilishim')),
            ],
            options={
                'verbose_name': 'About',
                'verbose_name_plural': 'Aboutour',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Ism')),
                ('subject', models.TextField(verbose_name='Subject')),
                ('email', models.EmailField(max_length=254, verbose_name='Email manzil')),
                ('message', models.TextField(blank=True, verbose_name='Xabar')),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contacts',
            },
        ),
        migrations.CreateModel(
            name='Rasmlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rasm', models.ImageField(null=True, upload_to='', verbose_name='Rasm')),
            ],
            options={
                'verbose_name': 'Rasm',
                'verbose_name_plural': 'Rasmlar',
            },
        ),
        migrations.AlterModelOptions(
            name='lesson_9',
            options={'verbose_name': 'Lesson', 'verbose_name_plural': 'Lessons'},
        ),
        migrations.AlterModelOptions(
            name='mediauser',
            options={'verbose_name': 'MediaUser', 'verbose_name_plural': 'MediaUsers'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Post', 'verbose_name_plural': 'Postlar'},
        ),
        migrations.AddField(
            model_name='mediauser',
            name='testiomonial',
            field=models.TextField(default='Bu dizayner haqida yaxshi fikrdaman', verbose_name='Sharh'),
        ),
        migrations.AddField(
            model_name='mediauser',
            name='work',
            field=models.CharField(default=2, max_length=50, verbose_name='Kasbi'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='lesson_9',
            name='content',
            field=models.TextField(blank=True, default="Bu haqida to'liq ma'lumot topa olmadik", verbose_name='Matn'),
        ),
        migrations.AlterField(
            model_name='lesson_9',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Iconka'),
        ),
        migrations.AlterField(
            model_name='mediauser',
            name='first_name',
            field=models.CharField(max_length=30, verbose_name='Familiyasi'),
        ),
        migrations.AlterField(
            model_name='mediauser',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Rasmi'),
        ),
        migrations.AlterField(
            model_name='mediauser',
            name='last_name',
            field=models.CharField(max_length=30, verbose_name='Ismi'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Rasmi'),
        ),
        migrations.AlterField(
            model_name='post',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='media.mediauser', verbose_name='Yaratuvchi'),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(verbose_name='Matn'),
        ),
    ]