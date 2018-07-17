from django.contrib import admin
from .models import Artist, Events, News, Releases, Merchandise, Testimonials, Services, Type_of_Event, Talent, Genre

# Register your models here.
admin.site.register(Artist)
admin.site.register(Events)
admin.site.register(News)
admin.site.register(Releases)
admin.site.register(Merchandise)
admin.site.register(Testimonials)
admin.site.register(Services)
admin.site.register(Type_of_Event)
admin.site.register(Talent)
admin.site.register(Genre)
