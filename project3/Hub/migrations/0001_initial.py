# Generated by Django 3.2 on 2022-02-07 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=50, verbose_name='Titre du projet')),
                ('project_duration', models.IntegerField(default=0, verbose_name='duree Estimee')),
                ('time_allocated', models.IntegerField(verbose_name='temps alloue')),
                ('needs', models.TextField(max_length=250, verbose_name='Besoins')),
                ('description', models.TextField(max_length=250)),
                ('isValid', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=100)),
                ('LastName', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Hub.user')),
            ],
            bases=('Hub.user',),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Hub.user')),
            ],
            bases=('Hub.user',),
        ),
        migrations.CreateModel(
            name='MembershipInProjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_allocated', models.IntegerField()),
                ('Project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hub.project')),
                ('Student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hub.student')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='creator',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Project_Owner', to='Hub.student'),
        ),
        migrations.AddField(
            model_name='project',
            name='members',
            field=models.ManyToManyField(blank=True, related_name='les_membres', through='Hub.MembershipInProjects', to='Hub.Student'),
        ),
        migrations.AddField(
            model_name='project',
            name='supervisor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='project_Coach', to='Hub.coach'),
        ),
    ]