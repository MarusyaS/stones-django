# Generated by Django 4.1 on 2023-02-20 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inscription',
            fields=[
                ('ID', models.CharField(max_length=6, primary_key=True, serialize=False, unique=True)),
                ('Name', models.TextField()),
                ('NameVariations', models.TextField()),
                ('ContextType', models.TextField()),
                ('DigitalDocumentation', models.TextField()),
                ('CitDTS', models.CharField(max_length=10)),
                ('CitVasilev', models.CharField(max_length=10)),
                ('CitBazylhan', models.CharField(max_length=10)),
                ('CitKormushin', models.CharField(max_length=10)),
                ('LAT', models.FloatField(null=True)),
                ('LON', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Museum',
            fields=[
                ('MusID', models.CharField(max_length=6, primary_key=True, serialize=False, unique=True)),
                ('Name', models.CharField(max_length=30)),
                ('OfficialName', models.TextField()),
                ('InstitutionClass', models.TextField()),
                ('LAT', models.FloatField()),
                ('LON', models.FloatField()),
                ('Dates', models.DateField()),
                ('Docnumber', models.IntegerField()),
                ('Docmethod', models.TextField()),
                ('Description', models.TextField()),
                ('Country', models.TextField()),
                ('Adress', models.TextField()),
                ('Link', models.URLField(max_length=128)),
                ('Showing', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('ID', models.CharField(max_length=5, primary_key=True, serialize=False, unique=True)),
                ('NameToponim', models.CharField(max_length=30)),
                ('NamePerson', models.TextField()),
                ('NameVariations', models.TextField()),
                ('Type', models.TextField()),
                ('FirstNotion', models.TextField()),
                ('YearExcavate', models.IntegerField()),
                ('Country', models.TextField()),
                ('Region', models.TextField()),
                ('Area', models.TextField()),
                ('LAT', models.FloatField(null=True)),
                ('LON', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Model3D',
            fields=[
                ('ID', models.CharField(max_length=6, primary_key=True, serialize=False, unique=True)),
                ('Object', models.TextField()),
                ('Process', models.TextField()),
                ('Camera', models.TextField()),
                ('Lens', models.TextField()),
                ('FrameCount', models.IntegerField()),
                ('Scheme', models.TextField()),
                ('Date', models.DateField()),
                ('PolygonCount', models.IntegerField()),
                ('PolygonCM', models.FloatField()),
                ('Link', models.URLField(blank=True, db_index=True, max_length=128, verbose_name='ModelID')),
                ('Inscription', models.ForeignKey(blank=True, db_column='Inscription_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to='stonelib.inscription')),
                ('Site', models.ForeignKey(blank=True, db_column='Site_id', db_constraint=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to='stonelib.museum')),
            ],
        ),
        migrations.AddField(
            model_name='inscription',
            name='Site',
            field=models.ForeignKey(blank=True, db_column='Site_id', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sites', to='stonelib.site'),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('ID', models.CharField(max_length=5, primary_key=True, serialize=False, unique=True)),
                ('Type', models.TextField()),
                ('AdditionalDescription', models.TextField()),
                ('Link', models.URLField(blank=True, db_index=True, max_length=128)),
                ('Inscription', models.ForeignKey(blank=True, db_column='Inscription_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to='stonelib.inscription')),
            ],
        ),
    ]
