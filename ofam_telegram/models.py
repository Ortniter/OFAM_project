from django.db import models
from django.utils.translation import gettext as _
from adminsortable.models import SortableMixin


class DetailModel(SortableMixin, models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField()
    detail_url = models.URLField()
    detail_url_text = models.CharField(max_length=32)
    image_url = models.URLField()
    image = models.ImageField(upload_to='images', blank=False, null=True)
    the_order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    class Meta:
        abstract = True


class MainMenuButtonModel(DetailModel):
    class Meta:
        verbose_name = _('Main menu button')
        ordering = ['the_order']

    def __str__(self):
        return self.title


class EventModel(DetailModel):
    price = models.IntegerField()

    class Meta:
        verbose_name = _('Event')
        ordering = ['the_order']

    def __str__(self):
        return self.title


class ExhibitionModel(DetailModel):
    class Meta:
        verbose_name = _('Exhibition')
        ordering = ['the_order']

    def __str__(self):
        return self.title


class VisitModel(DetailModel):
    class Meta:
        verbose_name = _('Visit')
        ordering = ['the_order']

    def __str__(self):
        return self.title


class ShopProductModel(SortableMixin, models.Model):
    title = models.CharField(max_length=126)
    price = models.IntegerField()
    description = models.TextField()
    link_to_website = models.URLField()
    image_url = models.URLField()
    the_order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    class Meta:
        verbose_name = _('Shop Product')
        ordering = ['the_order']

    def __str__(self):
        return self.title


class TelegramUser(SortableMixin, models.Model):
    chat_id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=124, blank=True, null=True)
    first_name = models.CharField(max_length=124, blank=True, null=True)
    language_code = models.CharField(max_length=10, blank=True, null=True)
    sticker_message = models.IntegerField(blank=True, null=True)
    the_order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    class Meta:
        verbose_name = _('Telegram User')
        ordering = ['the_order']

    def __str__(self):
        return f'{self.username}: {self.chat_id}'
