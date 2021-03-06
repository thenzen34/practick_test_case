from datetime import datetime

from django.db import models


class News(models.Model):
    subject = models.CharField(
        max_length=256,
        verbose_name=u'Заголовок',
        blank=True, default=''
    )

    content = models.TextField(
        verbose_name=u'Контент',
    )

    date = models.DateField(
        verbose_name=u'Дата публикации',
        null=True, blank=True
    )

    class Meta:
        verbose_name = 'Новости'
        indexes = [
            models.Index(fields=['date']),
        ]
        ordering = ('date',)

    @staticmethod
    def getAllActive():
        today = datetime.now()
        return News.objects.filter(date__isnull=False).filter(date__lte=today).order_by('-date').all()
