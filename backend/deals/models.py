from django.db import models
from clients.models import Client
from media.models import Media


class Deal(models.Model):
    deal_id = models.AutoField(primary_key=True)
    deal_client = models.ForeignKey(Client, on_delete=models.CASCADE, blank=False)  # Client ID
    deal_brand = models.CharField(max_length=64, null=False, blank=False)
    deal_media = models.ForeignKey(Media, on_delete=models.CASCADE, blank=False, null=True)  # Media ID
    deal_sum = models.FloatField(null=False, blank=False)
    deal_time = models.FloatField(blank=False, null=False)
    deal_period = models.TextField(blank=False, null=False)  # Example: '11/11/2017-15/11/2017;17/11/2017-30/11/2017;'
    deal_paid = models.FloatField(blank=False, null=False, default=0)
    # ------------------
    # Possible deal's types:
    # '0' - Размещение
    # '1' - Сбыт
    # '2' - Изготовление
    # '3' - Реализация
    # '4' - Бартер
    # ------------------
    deal_type = models.CharField(max_length=1, null=False, blank=False)
    # ------------------
    # Possible deal's statuses:
    # '0' - В обработке
    # '1' - Ожидается оплата
    # '2' - Оплачена
    # '3' - Активна
    # '4' - Завершена
    # ------------------
    deal_status = models.CharField(max_length=1, null=False, blank=False, default='1')

    def change_paid_value(self, change: int):
        self.deal_paid += change
        if self.deal_status != '2' and self.deal_sum <= self.deal_paid:
            self.deal_status = '2'
        elif self.deal_status != '1' and self.deal_sum >= self.deal_paid:
            self.deal_status = '1'
        self.save()
