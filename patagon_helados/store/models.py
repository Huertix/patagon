from django.db import models

PAGES = [
    ('Menu', 'Menu'),
    ('Footer', 'Footer'),
    ('Page1', 'Page1'),
    ('Page2', 'Page2'),
    ('Page3', 'Page3'),
    ('Page4', 'Page4'),
    ('Page5', 'Page5')
]

class Image(models.Model):
    page = models.CharField(
        max_length=10,
        choices=PAGES,
        default='1'
    )
    name = models.CharField(max_length=500)
    imagefile = models.FileField(upload_to='images/', null=True, verbose_name="")

    def __str__(self):
        return self.page + ": " + self.name + ": " + str(self.imagefile)


class Text(models.Model):
    LANGUAGES = [
        ('EN', 'English'),
        ('DE', 'Deutsche'),
        ('ES', 'Espanol')
    ]
    page = models.CharField(
        max_length=10,
        choices=PAGES,
        default='1'
    )
    name = models.CharField(max_length=500)
    text = models.TextField(max_length=500)
    language = models.CharField(
        max_length=2,
        choices=LANGUAGES,
        default='DE'
    )

    def __str__(self):
        return self.page + ": " + self.language + ": " +self.name + ": " + str(self.text)
