from django.db import migrations


def forwards_func(apps, schema_editor):
    # Get model
    Courses = apps.get_model("mainapp", "Courses")
    # Create model's objects
    Courses.objects.create(
        name="Python для чайников",
        description="Мощный питонист из люблго одноклеточного за пол года!",
        cost="20000",
    )
    Courses.objects.create(
        name="Неистовый фронт-ендер!",
        description="Какие-то смешные 10000, и Javascript у ваших ног!",
        cost="10000",
    )


def reverse_func(apps, schema_editor):
    # Get model
    Courses = apps.get_model("mainapp", "Courses")
    # Delete objects
    Courses.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]
