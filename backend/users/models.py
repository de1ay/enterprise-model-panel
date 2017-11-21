from django.db import models


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_login = models.CharField(max_length=64, blank=False, null=False)
    user_name = models.CharField(max_length=64, blank=False, null=False)  # Full name
    user_password = models.CharField(max_length=256, blank=False, null=False)  # SHA-3
    # -------------------------
    # Possible user's accesses:
    # '0' - Admin
    # '1' - Enterprise admin
    # '2' - Employee
    # -------------------------
    user_access = models.CharField(max_length=1, blank=False, null=False)