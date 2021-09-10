from django.contrib import admin

# Register your models here.
from .models import akun
from .models import paslon
from .models import votemasuk
admin.site.register(akun)
admin.site.register(paslon)
admin.site.register(votemasuk)