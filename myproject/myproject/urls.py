# from django.contrib import admin
# from django.urls import path
# from myapp.views import test_signal, test_transaction

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('signal/', test_signal),
#     path('transaction/', test_transaction),
# ]


from django.contrib import admin
from django.urls import path
from myapp.views import test_signal, test_transaction

urlpatterns = [
    path('', test_signal),  # 👈 ADD THIS LINE
    path('admin/', admin.site.urls),
    path('signal/', test_signal),
    path('transaction/', test_transaction),
]