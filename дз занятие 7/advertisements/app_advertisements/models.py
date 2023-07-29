from django.db import models

# Create your models here.

class Advertisement(models.Model):
    title = models.CharField(verbose_name='заголовок', max_length=128)
    description = models.TextField('описание объявления')
    price = models.DecimalField('цена', max_digits=10, decimal_places=2)
    auction = models.BooleanField('возможность торга', help_text='Отметьте, если торг уместен')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'advertisements'

    def __str__(self):
        return f'Advertisement(id={self.id}, title={self.title}, price={self.price})'