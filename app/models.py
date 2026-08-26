from django.db import models


# Create your models here.
class AdminMaster(models.Model):
    ad_id = models.AutoField(primary_key=True, unique=True)
    ad_name = models.CharField(max_length=100)
    ad_mobile = models.CharField(max_length=100)
    ad_email = models.CharField(max_length=100)
    ad_password = models.CharField(max_length=100)
    ad_role = models.CharField(max_length=100, default="")
    ad_status = models.IntegerField(default=0)
    ad_created_by = models.CharField(max_length=100, default="")


class AddProducts(models.Model):
    ap_id = models.AutoField(primary_key=True, unique=True)
    ap_category = models.CharField(max_length=100, default="")
    ap_sub_category = models.CharField(max_length=100, default="")
    ap_name = models.CharField(max_length=100)
    ap_price = models.CharField(max_length=100)
    ap_quantity = models.CharField(max_length=100)
    ap_image = models.ImageField(upload_to="app/static/media/images/", default="")
    ap_description = models.CharField(max_length=100)
    # ad_role = models.CharField(max_length=100)
    ap_status = models.IntegerField(default=0)
    ap_role = models.CharField(max_length=100, default="")
    ap_created_by = models.CharField(max_length=100, default="")
    ap_created_name = models.CharField(max_length=100, default="")


class Order(models.Model):
    or_id = models.AutoField(primary_key=True, unique=True)
    or_name = models.CharField(max_length=100)
    or_weight = models.CharField(max_length=100)
    or_rate = models.CharField(max_length=100)
    or_total_amount = models.CharField(max_length=100)
    or_address = models.CharField(max_length=100)
    or_ordered_by = models.CharField(max_length=100)
    or_date = models.CharField(max_length=100)
    or_transaction_id = models.CharField(max_length=100)
    or_status = models.CharField(max_length=100, default=0)
    or_created_by = models.CharField(max_length=100)


class Shipping(models.Model):
    sh_id = models.AutoField(primary_key=True, unique=True)
    sh_shipping_status = models.CharField(max_length=100)
    sh_ordered_by = models.CharField(max_length=100)
    sh_status = models.CharField(max_length=100)
    sh_created_by = models.CharField(max_length=100)


class Cart(models.Model):
    ct_id = models.AutoField(primary_key=True, unique=True)
    ct_name = models.CharField(max_length=100)
    ct_image = models.CharField(max_length=100)
    ct_weight = models.CharField(max_length=100)
    ct_price = models.CharField(max_length=100)
    ct_total_amount = models.IntegerField()
    ct_ordered_by = models.CharField(max_length=100)
    ct_status = models.CharField(max_length=100)
    ct_created_by = models.CharField(max_length=100)


class Review(models.Model):
    rv_id = models.AutoField(primary_key=True, unique=True)
    rv_ap_id = models.CharField(max_length=100)
    rv_name = models.CharField(max_length=100)
    rv_email = models.CharField(max_length=100)
    rv_message = models.CharField(max_length=100)
    rv_status = models.CharField(max_length=100)


class Register(models.Model):
    rg_id = models.AutoField(primary_key=True, unique=True)
    rg_name = models.CharField(max_length=100)
    rg_mobile = models.CharField(max_length=100)
    rg_email = models.CharField(max_length=100)
    rg_password = models.CharField(max_length=100)
    rg_address = models.CharField(max_length=100, default="")
    rg_status = models.CharField(max_length=100)


# class Category(models.Model):
# 	cg_id = models.AutoField(primary_key=True, unique = True)
# 	cg_name = models.CharField(max_length=100)
# 	cg_status = models.CharField(max_length=100, default=0)


class PurchasedProducts(models.Model):
    ps_id = models.AutoField(primary_key=True, unique=True)
    ps_or_id = models.CharField(max_length=100)
    ps_product_name = models.CharField(max_length=100)
    ps_image = models.CharField(max_length=100)
    ps_weight = models.CharField(max_length=100)
    ps_price = models.CharField(max_length=100)
    ps_total_amt = models.CharField(max_length=100)
    ps_date = models.CharField(max_length=100)
    ps_status = models.CharField(max_length=100)
    ps_user_name = models.CharField(max_length=100)
    ps_user_email = models.CharField(max_length=100)
    ps_vendor_email = models.CharField(max_length=100)


class VendorProduct(models.Model):
    vp_id = models.AutoField(primary_key=True, unique=True)
    vp_name = models.CharField(max_length=100, default="")
    vp_price = models.CharField(max_length=100, default="")
    vp_quantity = models.CharField(max_length=100, default="")
    vp_image = models.ImageField(upload_to="app/static/media/images/", default="")
    vp_description = models.CharField(max_length=100, default="")
    # ad_role = models.CharField(max_length=100)
    vp_status = models.IntegerField(default=0)
    vp_created_by = models.CharField(max_length=100, default="")


class Category(models.Model):
    ca_id = models.AutoField(primary_key=True, unique=True)
    ca_name = models.CharField(max_length=100, default="")
    ca_status = models.CharField(max_length=100, default="")
    ca_created_by = models.CharField(max_length=100, default="")


# class SubCategory(models.Model):
# 	sc_id = models.AutoField(primary_key=True, unique = True)
# 	sc_category = models.CharField(max_length=100,default="")
# 	sc_name = models.CharField(max_length=100,default="")
# 	sc_status = models.CharField(max_length=100,default="")
# 	sc_created_by = models.CharField(max_length=100,default="")


class ForgotPassword(models.Model):
    fp_id = models.AutoField(primary_key=True, unique=True)
    fp_email = models.CharField(max_length=100, default="")
    fp_otp = models.CharField(max_length=100, default="")
