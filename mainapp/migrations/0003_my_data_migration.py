from django.db import migrations


def forwards_func(apps, schema_editor):
    # Get model
    News = apps.get_model("mainapp", "News")
    # Create model's objects
    News.objects.create(
        title="Появился медведь",
        preambule="Опасного хищника заметили жители города N",
        body="Короче, появился медведь — и все, лес стал на четыре часа больше.",
    )
    News.objects.create(
        title="Упали цены на пиво.",
        preambule="Нож в спину пролетариата!",
        body="За неделю в России снизились цены на некоторые виды пива. Об этом свидетельствуют данные федеральной службы по тарифам. За период с 11 по 17 ноября 2013 года средняя цена за литр пива в супермаркетах снизилась на 1,9% до 64,3 рубля. Стоимость литра пива в магазинах и на оптовых рынках снизилась на 0,6% до 60,2 рубля, а на рознице в кафе и ресторанах - на 2% до 61,4 рубля за литр. Напомним, что в начале октября 2013 года стоимость литра пива составляла в среднем около 79 рублей.",
    )
    News.objects.create(
        title="Пропала корова",
        preambule="Снова ЧП в городе N!",
        body="Помогите найти! В районе перекрестка улиц Зари и Мира пропала корова. Корове около года, рыжая, хвост коричневый. У коровы есть клеймо на правом боку. Если кто-то видел или владеет информацией о местонахождении животного, позвоните по телефону 8-926-214-53-81. Пожалуйста! Источник В доме появился новый житель. Котёнок, мальчик, возраст примерно 1,5 месяца. Окрас-чёрный с белым. Приучен к лотку. Очень ласковый и игривый. Отдаем только в добрые руки, с ненавязчивым отслеживанием судьбы.",
    )
    News.objects.create(
        title="Прогноз погоды",
        preambule="Ожидаются сильные дожди",
        body="Ожидаются сильные дожди, грозы и град, а ветер усилится до 23 м/с. Об этом сообщает Гидрометцентр России. По данным метеорологов, сегодня в Москве и Подмосковье ожидается облачная погода с прояснениями. Синоптики прогнозируют сильные дожди на территории столичного региона. При этом местами пройдет гроза. Ветер усилится порывами до 17-22 м/сек. Температура воздуха составит +25°С. В четверг, 16 июня, в столице также пройдут дожди с грозами. Днем воздух прогреется до +24°С",
    )


def reverse_func(apps, schema_editor):
    # Get model
    News = apps.get_model("mainapp", "News")
    # Delete objects
    News.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]