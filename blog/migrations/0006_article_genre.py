# Generated by Django 4.1.6 on 2023-03-09 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_article_created_article_updated_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='genre',
            field=models.CharField(choices=[('education', 'Education'), ('politcs', 'Politics'), ('movie', 'Movie'), ('scifi', 'Science Ficiton')], default='education', max_length=50),
        ),
    ]
