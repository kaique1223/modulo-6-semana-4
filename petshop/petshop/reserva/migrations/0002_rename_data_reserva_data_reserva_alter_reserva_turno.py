# Generated by Django 4.2.6 on 2023-11-21 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserva', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reserva',
            old_name='data',
            new_name='data_reserva',
        ),
        migrations.AlterField(
            model_name='reserva',
            name='turno',
            field=models.CharField(choices=[('MANHÃ', 'Manhã'), ('TARDE', 'Tarde')], max_length=50, verbose_name='turno'),
        ),
    ]