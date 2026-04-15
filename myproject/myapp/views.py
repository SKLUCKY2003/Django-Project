from django.http import HttpResponse
from django.db import transaction
from .models import TestModel
import time
import threading


# ✅ TEST 1: SYNCHRONOUS + SAME THREAD
def test_signal(request):
    print("\n===== VIEW START =====")

    print("View Thread ID:", threading.get_ident())

    start = time.time()

    TestModel.objects.create(name="Sync Test")

    end = time.time()

    print("===== VIEW END =====\n")

    return HttpResponse(f"Time taken: {round(end - start, 2)} seconds")


# ✅ TEST 2: TRANSACTION CHECK
def test_transaction(request):
    try:
        with transaction.atomic():
            TestModel.objects.create(name="Transaction Test")
            raise Exception("Force rollback")
    except:
        pass

    count = TestModel.objects.count()

    return HttpResponse(f"Objects in DB: {count}")