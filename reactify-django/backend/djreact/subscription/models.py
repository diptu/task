# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Subscription(models.Model):
    create_date = models.CharField(max_length=255, blank=True, null=True)
    subscription_on = models.CharField(max_length=255, blank=True, null=True)
    transaction_on = models.CharField(max_length=255, blank=True, null=True)
    event_time = models.CharField(max_length=255, blank=True, null=True)
    transaction_completed_on = models.CharField(max_length=255, blank=True, null=True)
    transaction_id = models.CharField(max_length=255, blank=True, null=True)
    membership_no = models.CharField(max_length=255, blank=True, null=True)
    previous_product_code = models.CharField(max_length=255, blank=True, null=True)
    current_product_code = models.CharField(max_length=255, blank=True, null=True)
    retailer_type = models.CharField(max_length=255, blank=True, null=True)
    retailer_area = models.CharField(max_length=255, blank=True, null=True)
    retailer_pos_code = models.CharField(max_length=255, blank=True, null=True)
    subscription_status = models.CharField(max_length=255, blank=True, null=True)
    user_type = models.CharField(max_length=255, blank=True, null=True)
    payment_type = models.CharField(max_length=255, blank=True, null=True)
    subscription_type = models.CharField(max_length=255, blank=True, null=True)
    subscription_channel = models.CharField(max_length=255, blank=True, null=True)
    transaction_channel = models.CharField(max_length=255, blank=True, null=True)
    user_type1 = models.CharField(max_length=255, blank=True, null=True)
    parent_membership_no = models.CharField(max_length=255, blank=True, null=True)
    relationship_with_parent = models.CharField(max_length=255, blank=True, null=True)
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'subscription_data'