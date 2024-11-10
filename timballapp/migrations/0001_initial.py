# Generated by Django 5.0.6 on 2024-05-16 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apuesta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IdApiFixture', models.IntegerField()),
                ('IdApiBookmaker', models.IntegerField()),
                ('IdApiApuesta', models.IntegerField()),
                ('Nombre', models.CharField(max_length=200)),
                ('Tipo', models.CharField(max_length=200)),
                ('Multiplicador', models.IntegerField()),
                ('Porcentaje', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Bookmaker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Bookmaker', models.IntegerField()),
                ('Nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Competiciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IdApiComp', models.IntegerField()),
                ('IdApiPais', models.IntegerField()),
                ('Nombre', models.CharField(max_length=200)),
                ('Image_URL', models.CharField(max_length=200)),
                ('Temporada', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IdApiEquipo', models.IntegerField()),
                ('IdApiComp', models.IntegerField()),
                ('Nombre', models.CharField(max_length=200)),
                ('IdApiEstadio', models.IntegerField()),
                ('IdApiPais', models.IntegerField()),
                ('Image_URL', models.CharField(max_length=200)),
                ('Fundacion', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Estadio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IdApiEstadio', models.IntegerField()),
                ('Nombre', models.CharField(max_length=200)),
                ('Ciudad', models.CharField(max_length=200)),
                ('Direccion', models.CharField(max_length=200)),
                ('Capacidad', models.IntegerField()),
                ('Image_URL', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Fixture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IdApiFixture', models.IntegerField()),
                ('Arbitro', models.CharField(max_length=200)),
                ('Fecha', models.DateField()),
                ('Hora', models.TimeField()),
                ('IdApiEstadio', models.IntegerField()),
                ('IdEquipoLocal', models.IntegerField()),
                ('IdEquipoVisitante', models.IntegerField()),
                ('Status', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Jugador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IdApiJugador', models.IntegerField()),
                ('Nombre', models.CharField(max_length=200)),
                ('Edad', models.IntegerField()),
                ('Nacionalidad', models.CharField(max_length=200)),
                ('Altura', models.CharField(max_length=200)),
                ('Peso', models.CharField(max_length=200)),
                ('Image_URL', models.CharField(max_length=200)),
                ('IdApiEquipo', models.IntegerField()),
                ('Posicion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=200)),
                ('Image_URL', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Tecnico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IdApiTecnico', models.IntegerField()),
                ('Nombre', models.CharField(max_length=200)),
                ('Edad', models.IntegerField()),
                ('Nacionalidad', models.CharField(max_length=200)),
                ('Altura', models.CharField(max_length=200)),
                ('Peso', models.CharField(max_length=200)),
                ('Image_URL', models.CharField(max_length=200)),
                ('IdApiEquipo', models.IntegerField()),
            ],
        ),
    ]