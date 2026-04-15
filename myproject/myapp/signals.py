from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import TestModel
import time
import threading

@receiver(post_save, sender=TestModel)
def my_signal(sender, instance, **kwargs):
    print("\n----- SIGNAL START -----")

    # THREAD CHECK
    print("Signal Thread ID:", threading.get_ident())

    # DELAY → proves synchronous
    time.sleep(3)

    print("Signal executed for:", instance.name)
    print("----- SIGNAL END -----\n")