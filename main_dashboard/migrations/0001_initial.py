# Generated by Django 4.1.1 on 2022-10-01 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thematic_area', models.CharField(choices=[('SRHR', 'SRHR'), ('HIV/TB', 'HIV/TB'), ('WLPR', 'WLPR'), ('SILU', 'SILU'), ('H&G', 'H&G')], max_length=100, verbose_name='Choose Persons')),
                ('donor', models.CharField(blank=True, max_length=200, null=True, verbose_name='Donor')),
                ('project_name', models.CharField(max_length=200, verbose_name='Project Name')),
                ('log', models.ImageField(upload_to='')),
                ('info', models.TextField()),
                ('person_responsible', models.CharField(choices=[('Timoty', 'Timothy'), ('Lisa', 'Lisa'), ('Tara', 'Tara'), ('Jesica', 'Jesica'), ('Mitchelle', 'Mitchelle'), ('Nyokabi', 'Nyokabi'), ('Dorcas', 'Dorcas'), ('Ken', 'Ken'), ('Martha', 'Martha')], max_length=100, verbose_name='Choose Persons')),
                ('frequency', models.CharField(choices=[('Annual', 'Annual'), ('Bi-annual', 'Bi-annual')], max_length=100, verbose_name='Choose Persons')),
                ('project_start', models.DateField()),
                ('project_end', models.DateField()),
                ('value', models.IntegerField()),
                ('currency', models.CharField(choices=[('USD', 'USD'), ('Ksh', 'Ksh')], max_length=100, verbose_name='Choose Currency')),
            ],
        ),
    ]