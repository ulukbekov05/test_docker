

import multiselectfield.db.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_movie_movie_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='types',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('144', '144'), ('360', '360'), ('480', '480'), ('720', '720'), ('1080', '1080')], max_length=45),
        ),
    ]
