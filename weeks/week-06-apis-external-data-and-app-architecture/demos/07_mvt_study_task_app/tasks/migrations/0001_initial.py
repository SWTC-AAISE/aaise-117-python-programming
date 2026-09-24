from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="StudyTask",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("course_name", models.CharField(max_length=80)),
                ("title", models.CharField(max_length=120)),
                ("estimated_minutes", models.PositiveIntegerField()),
            ],
        ),
    ]
