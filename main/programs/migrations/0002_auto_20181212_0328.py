# Generated by Django 2.1.4 on 2018-12-12 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=300, null=True)),
                ('location', models.CharField(blank=True, max_length=200, null=True)),
                ('codebase', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'C++'), (2, 'C#'), (3, 'Python'), (4, 'ASP.NET'), (5, 'JAVA'), (6, 'VB.NET'), (7, 'VB')], null=True)),
                ('last_commit_time', models.DateTimeField(blank=True, null=True)),
                ('last_commit_user', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Book',
        ),
    ]
