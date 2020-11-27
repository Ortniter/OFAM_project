from django.contrib import admin
from .models import MainMenuButtonModel, EventModel, ExhibitionModel, VisitModel, ShopProductModel, TelegramUser
from adminsortable.admin import SortableAdmin

admin.site.register(MainMenuButtonModel, SortableAdmin)
admin.site.register(ShopProductModel, SortableAdmin)
admin.site.register(TelegramUser, SortableAdmin)

admin.site.register(ExhibitionModel, SortableAdmin)
admin.site.register(EventModel, SortableAdmin)
admin.site.register(VisitModel, SortableAdmin)
