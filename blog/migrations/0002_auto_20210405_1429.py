# Generated by Django 3.1.6 on 2021-04-05 08:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('Sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('author', models.CharField(max_length=13)),
                ('slug', models.CharField(max_length=130)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('img', models.ImageField(default='blogImg/2.jpg', upload_to='blogImg')),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
        migrations.RenameField(
            model_name='blogcomment',
            old_name='postno',
            new_name='Sno',
        ),
        migrations.AlterField(
            model_name='blogcomment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.post'),
        ),
        migrations.DeleteModel(
            name='Posts',
        ),
    ]
