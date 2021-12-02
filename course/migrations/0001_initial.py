# Generated by Django 3.2.9 on 2021-12-02 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('idcategorias', models.AutoField(db_column='idCategorias', primary_key=True, serialize=False)),
                ('descripcion', models.CharField(blank=True, db_column='Descripcion', max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('idclientes', models.AutoField(primary_key=True, serialize=False)),
                ('nombres', models.CharField(db_column='Nombres', max_length=45)),
                ('apellidos', models.CharField(db_column='Apellidos', max_length=45)),
                ('direccion', models.CharField(blank=True, db_column='Direccion', max_length=150, null=True)),
                ('telefono', models.CharField(blank=True, db_column='Telefono', max_length=45, null=True)),
                ('idcategorias', models.IntegerField(blank=True, db_column='idCategorias', null=True)),
                ('idzona', models.IntegerField(blank=True, db_column='idZona', null=True)),
                ('comentario', models.CharField(blank=True, db_column='Comentario', max_length=300, null=True)),
                ('idestado', models.IntegerField(blank=True, db_column='idEstado', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('idestado', models.AutoField(db_column='idEstado', primary_key=True, serialize=False)),
                ('descripcion', models.CharField(blank=True, db_column='Descripcion', max_length=45, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Zona',
            fields=[
                ('idzona', models.AutoField(db_column='idZona', primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=80, null=True)),
            ],
        ),
    ]
