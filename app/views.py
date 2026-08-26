from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from app.models import AdminMaster
from app.models import AddProducts
from app.models import Register
from app.models import Order
from app.models import Cart
from app.models import VendorProduct
from app.models import PurchasedProducts
from app.models import Category, ForgotPassword
from django.conf import settings
from django.core.mail import send_mail

# from app.models import SubCategory

from django.db.models import Sum

import datetime

# Create your views here.


def openHome(request):
    return render(request, "web/index.html")


def viewAbout(request):
    return render(request, "web/about.html")


def viewShop(request):
    return render(request, "web/shop.html")


def viewGalley(request):
    return render(request, "web/gallery.html")


def viewContact(request):
    return render(request, "web/contact.html")


def viewLogin(request):
    return render(request, "web/login.html")


def viewRegister(request):
    return render(request, "web/register.html")


def viewCart(request):
    return render(request, "web/cart.html")


def viewCheckOut(request):
    return render(request, "web/checkout.html")


def viewShopDetails(request):
    return render(request, "web/shop-details.html")

def viewOrderHistory(request):
    if "web_email" in request.session:
        return render(request, "web/order_history.html", {})
    else:
        return redirect("/login/")


def viewSingleProduct(request):
    return render(request, "web/product-single.html")


def paymentSuccess(request):
    return render(request, "web/pay-success.html")


def getcategoryDetails(request):
    return render(request, "web/category_detail.html")


# admin
def adminIndex(request):
    lclTotalOrders = Order.objects.filter().count()
    lclTotalUsers = Register.objects.filter().count()
    lclTotalRevenue = (
        Order.objects.filter().aggregate(total=Sum("or_total_amount"))["total"]
        or Decimal()
    )

    context = {}
    context["lclTotalOrders"] = lclTotalOrders
    context["lclTotalUsers"] = lclTotalUsers
    context["lclTotalRevenue"] = lclTotalRevenue
    return render(request, "admin/index_admin.html", context)


def adminAdd_admin(request):
    return render(request, "admin/add_admin.html")


def adminAdd_vendor(request):
    return render(request, "admin/add_vendor.html")


def adminOrders(request):
    return render(request, "admin/view_orders.html")


def adminProduct(request):
    return render(request, "admin/view_product.html")


def adminUsers(request):
    return render(request, "admin/view_users.html")


def adminPayment(request):
    return render(request, "admin/view_payment.html")


def adminSignin(request):
    return render(request, "admin/auth-normal-sign-in.html")


def adminAdmin(request):
    return render(request, "admin/admin_master.html")


def adminProfile(request):
    return render(request, "admin/profile.html")


def vendor_profile(request):
    return render(request, "vendor/vendor_profile.html")


def web_profile(request):
    return render(request, "web/web_profile.html")


def addProduct(request):
    return render(request, "admin/add_product.html")


def adminLogin(request):
    return render(request, "admin/admin_login.html")


# vendor


def viewVendorIndex(request):
    return render(request, "vendor/vendor_index.html")


def viewAddProduct(request):
    return render(request, "vendor/vendor_product.html")


def viewUsers(request):
    return render(request, "vendor/vendor_users.html")


def viewVendorOrders(request):
    return render(request, "vendor/viewvendor_orders.html")


def viewCategories(request):
    return render(request, "admin/categories.html")


def subCategories(request):
    return render(request, "vendor/sub_categories.html")


# admin database


def viewAdminMaster(request):
    if request.POST["action"] == "add":
        AdminMaster.objects.create(
            ad_name=request.POST["txtName"],
            ad_mobile=request.POST["txtNumber"],
            ad_email=request.POST["txtEmail"],
            ad_password=request.POST["txtPassword"],
            ad_role=request.POST["selRole"],
        )

    elif request.POST["action"] == "getData":
        data = AdminMaster.objects.filter(ad_status="0").values()
        data = list(data)
        values = JsonResponse(data, safe=False)
        return values

    elif request.POST["action"] == "update":
        data = AdminMaster.objects.filter(ad_id=request.POST["id"]).update(
            ad_name=request.POST["txtName1"],
            ad_mobile=request.POST["txtMobileNo1"],
            ad_email=request.POST["txtEmail1"],
        )

    elif request.POST["action"] == "delete":
        data = AdminMaster.objects.filter(ad_id=request.POST["id"]).update(
            ad_status="1"
        )

    return HttpResponse()


def adminProfileData(request):
    data = AdminMaster.objects.filter(ad_email=request.session["email"]).values()
    data = list(data)
    values = JsonResponse(data, safe=False)
    return values


def userProfileData(request):
    data = Register.objects.filter(rg_email=request.session["web_email"]).values()
    data = list(data)
    values = JsonResponse(data, safe=False)
    return values


def adminUpdateProfileData(request):
    AdminMaster.objects.filter(ad_email=request.session["email"]).update(
        ad_name=request.POST["txtName"], ad_mobile=request.POST["txtNumber"]
    )

    return HttpResponse()


def updateUserProfile(request):
    Register.objects.filter(rg_email=request.session["web_email"]).update(
        rg_name=request.POST["txtName"],
        rg_mobile=request.POST["txtMobileNo"],
        rg_address=request.POST["txtAddress"],
    )
    return HttpResponse()


def checkAdminLogin(request):
    if AdminMaster.objects.filter(
        ad_email=request.POST["txtEmail"], ad_password=request.POST["txtPassword"]
    ).exists():
        data = AdminMaster.objects.filter(ad_email=request.POST["txtEmail"]).values()
        data = list(data)
        dictValue = data[0]
        request.session["email"] = dictValue["ad_email"]
        request.session["role"] = dictValue["ad_role"]
        request.session["name"] = dictValue["ad_name"]

        return HttpResponse(dictValue["ad_role"])
    else:
        return HttpResponse("10")


def checkWebLogin(request):
    if Register.objects.filter(
        rg_email=request.POST["txtEmail1"], rg_password=request.POST["txtPassword1"]
    ).exists():
        request.session["web_email"] = request.POST["txtEmail1"]
        return HttpResponse("1")
    else:
        return HttpResponse("10")


# Add products

# def viewOrganicProducts(request):
#     if request.POST['action'] == "add":
#         AddProducts.objects.create(
#             ap_name = request.POST['txtName'],
#             ap_price = request.POST['txtPrice'],
#             ap_quantity = request.POST['txtQuantity'],
#             ap_image = request.FILES['txtImage'],
#             ap_description = request.POST['txtDescription'],
#             ap_created_by = request.session['email'],

#         )

#     elif request.POST['action'] == "getData":
#         data = AddProducts.objects.filter(ap_status='0', ap_created_by=request.session['email']).values()
#         data = list(data)
#         values = JsonResponse(data, safe=False)
#         return values

#     elif request.POST['action'] == "update":
#         data = AddProducts.objects.filter(ap_id=request.POST['id']).update(ap_name = request.POST['txtName1'],ap_price = request.POST['txtPrice1'],ap_quantity = request.POST['txtQuantity1'],ap_description = request.POST['txtDescription1']);

#     elif request.POST['action'] == "delete":
#         data = AddProducts.objects.filter(ap_id=request.POST['id']).update(ap_status='1')

#     return HttpResponse()


def getProductDetails(request):
    data = AddProducts.objects.filter(ap_status="0").values()
    data = list(data)
    values = JsonResponse(data, safe=False)
    return values


def getSingleItem(request):
    products_json = AddProducts.objects.filter(ap_id=request.POST["txtID"]).values()
    data = list(products_json)
    value = JsonResponse(data, safe=False)
    return value


def addCart(request):
    if "web_email" in request.session:
        products_json = AddProducts.objects.filter(ap_id=request.POST["txtID"]).values()
        data = list(products_json)
        dictValue = data[0]
        request.session["vendor_email"] = dictValue["ap_created_by"]
        lclID = Cart.objects.count()
        status = "0"
        lclNewID = lclID + 1

        lclTotalAmt = float(request.POST["selQTY"]) * float(dictValue["ap_price"])

        Cart.objects.create(
            ct_id=lclNewID,
            ct_name=dictValue["ap_name"],
            ct_image=dictValue["ap_image"],
            ct_weight=request.POST["selQTY"],
            ct_price=dictValue["ap_price"],
            ct_total_amount=lclTotalAmt,
            ct_ordered_by=request.session["web_email"],
            ct_status=status,
            ct_created_by=dictValue["ap_created_by"],
        )
        return HttpResponse("1")
    else:
        return HttpResponse("0")


def getCart(request):
    cart_json = Cart.objects.filter(
        ct_status="0", ct_ordered_by=request.session["web_email"]
    ).values()
    data = list(cart_json)
    value = JsonResponse(data, safe=False)
    return value


def cancelItem(request):
    Cart.objects.filter(ct_id=request.POST["id"]).update(ct_status="1")
    return HttpResponse()


def checkoutPayment(request):
    lclID = Order.objects.count()
    status = "0"
    lclNewID = lclID + 1

    Order.objects.create(
        or_id=lclNewID,
        or_name=request.POST["txtName"],
        or_weight=0,
        or_rate=0,
        or_total_amount=request.POST["totalAmt"],
        or_address=request.POST["txtAddress"],
        or_date=request.POST["txtDate"],
        or_ordered_by=request.session["web_email"],
        or_status=status,
        or_created_by=request.session["vendor_email"],
    )

    productImage = request.POST["productImage"].split("<>")
    productQTY = request.POST["productQTY"].split("<>")
    productName = request.POST["productName"].split("<>")
    productPrice = request.POST["productPrice"].split("<>")
    productTotal = request.POST["productTotal"].split("<>")
    productVendor = request.POST["productVendor"].split("<>")
    k = 0

    for i in productQTY:
        lclID1 = PurchasedProducts.objects.count()
        status = "0"
        lclNewID1 = lclID1 + 1

        now = datetime.datetime.now()
        dateNow = now.strftime("%Y-%m-%d")

        PurchasedProducts.objects.create(
            ps_id=lclNewID1,
            ps_or_id=lclNewID,
            ps_product_name=productName[k],
            ps_image=productImage[k],
            ps_weight=productQTY[k],
            ps_price=productPrice[k],
            ps_total_amt=productTotal[k],
            ps_date=dateNow,
            ps_status=status,
            ps_vendor_email=productVendor[k],
            ps_user_name=request.POST["txtName"],
            ps_user_email=request.session["web_email"],
        )

        # product_json = Product.objects.filter(ap_name = productName[k]).values()
        # data = list(product_json)
        # dictValue = data[0]
        # print(dictValue);
        # Qty = dictValue['ap_total_quantity']

        # lclTotalQTY = int(Qty) - int(productQTY[k]);

        # Product.objects.filter(ap_name = productName[k]).update(ap_total_quantity = lclTotalQTY)
        k += 1

    return HttpResponse()


def checkCheckout(request):
    if "web_email" in request.session:
        return HttpResponse(request.POST["txtID"])
    else:
        return HttpResponse(0)


def getBuyNowURL(request):
    products_json = AddProducts.objects.filter(ap_id=request.POST["txtID"]).values()
    data = list(products_json)
    value = JsonResponse(data, safe=False)
    return value


def getOrderHistory(request):
    products_json = Order.objects.filter(
        or_ordered_by=request.session["web_email"]
    ).values()
    data = list(products_json)
    value = JsonResponse(data, safe=False)
    return value


def getUserData(request):
    products_json = Register.objects.filter().values()
    data = list(products_json)
    value = JsonResponse(data, safe=False)
    return value


def getOrderData(request):
    if request.session["role"] == "Admin":
        products_json = Order.objects.filter().values()
        data = list(products_json)
        value = JsonResponse(data, safe=False)
        return value
    else:
        products_json = PurchasedProducts.objects.filter(
            ps_vendor_email=request.session["email"]
        ).values()
        data = list(products_json)
        value = JsonResponse(data, safe=False)
        return value


def paymentSuccess(request):
    Order.objects.filter(
        or_ordered_by=request.session["web_email"], or_status="0"
    ).update(or_transaction_id=request.GET.get("transaction_id"), or_status="1")
    Cart.objects.filter(ct_ordered_by=request.session["web_email"]).update(
        ct_status="1"
    )
    return render(request, "web/pay_success.html", {})


def newRegister(request):
    if Register.objects.filter(
        rg_email=request.POST["txtEmail"], rg_mobile=request.POST["txtMobileNo"]
    ).exists():
        return HttpResponse("10")
    else:
        lclID = Register.objects.count()
        status = "0"
        lclNewID = lclID + 1

        Register.objects.create(
            rg_id=lclNewID,
            rg_name=request.POST["txtName"],
            rg_mobile=request.POST["txtMobileNo"],
            rg_email=request.POST["txtEmail"],
            rg_password=request.POST["txtPassword"],
            rg_address=request.POST["txtAddress"],
        )

        return HttpResponse("0")

    # vendor


# def viewVendorProduct(request):
#     if request.POST['action'] == "add":
#         VendorProduct.objects.create(
#             vp_name = request.POST['txtName'],
#             vp_price = request.POST['txtPrice'],
#             vp_quantity = request.POST['txtQuantity'],
#             vp_image = request.FILES['txtImage'],
#             vp_description = request.POST['txtDescription'],
#             vp_created_by = request.session['email'],

#         )

#     elif request.POST['action'] == "getData":
#         data = VendorProduct.objects.filter(vp_status='0', vp_created_by=request.session['email']).values()
#         # data = VendorProduct.objects.filter(vp_status='0').values()
#         data = list(data)
#         values = JsonResponse(data, safe=False)
#         return values

#     elif request.POST['action'] == "update":
#         data = VendorProduct.objects.filter(vp_id=request.POST['id']).update(vp_name = request.POST['txtName1'],vp_price = request.POST['txtPrice1'],vp_quantity = request.POST['txtQuantity1'],vp_description = request.POST['txtDescription1']);

#     elif request.POST['action'] == "delete":
#         data = VendorProduct.objects.filter(vp_id=request.POST['id']).update(vp_status='1')

#     return HttpResponse()


def viewCartCount(request):
    if "web_email" in request.session:
        cartCount = Cart.objects.filter(
            ct_ordered_by=request.session["web_email"], ct_status="0"
        ).count()
        return HttpResponse(cartCount)
    else:
        return 0


# CATEGORIES
def addCategory(request):
    # count collection
    lclID = Category.objects.count()
    status = "0"
    lclNewID = lclID + 1

    Category.objects.create(
        ca_id=lclNewID,
        ca_name=request.POST["txtName"],
        ca_status=status,
        ca_created_by=request.session["email"],
    )

    return HttpResponse()


def updateCategory(request):
    Category.objects.filter(ca_id=request.POST["id"]).update(
        ca_name=request.POST["txtName1"]
    )
    return HttpResponse()


def deleteCategory(request):
    Category.objects.filter(ca_id=request.POST["id"]).update(ca_status="1")
    return HttpResponse()


def getCategoryData(request):
    if request.session["role"] == "Vendor":
        category_json = Category.objects.filter(ca_status="0").values()
        data = list(category_json)
        value = JsonResponse(data, safe=False)
        return value
    else:
        category_json = Category.objects.filter(ca_status="0").values()
        data = list(category_json)
        value = JsonResponse(data, safe=False)
        return value


# SUB CATEGORY
# def addSubCategory(request):
# 	# count collection
# 	lclID = SubCategory.objects.count()
# 	status = "0"
# 	lclNewID = lclID + 1

# 	SubCategory.objects.create (
# 		sc_id = lclNewID,
# 		sc_category = request.POST['selCategory'],
# 		sc_name = request.POST['txtName'],
# 		sc_status = status,
# 		sc_created_by = request.session['email']

# 	)

# 	return HttpResponse()


# def updateSubCategory(request):
# 	SubCategory.objects.filter(sc_id = request.POST['id']).update(sc_category = request.POST['selCategory1'],sc_name = request.POST['txtName1'])
# 	return HttpResponse()


# def deleteSubCategory(request):
# 	SubCategory.objects.filter(sc_id = request.POST['id']).update(sc_status = "1")
# 	return HttpResponse()


# def getSubCategoryData(request):

# 	if request.session['role'] == "Vendor":
# 		subCategory_json = SubCategory.objects.filter(sc_status='0',sc_created_by=request.session['email']).values()
# 		data = list(subCategory_json)
# 		value = JsonResponse(data, safe=False)
# 		return value
# 	else:
# 		subCategory_json = SubCategory.objects.filter(sc_status='0',sc_created_by=request.session['email']).values()
# 		data = list(subCategory_json)
# 		value = JsonResponse(data, safe=False)
# 		return value

# ADD PRODUCT


def viewVendorProduct(request):
    # post = AdminMaster(first_name=request.POST.get("Karthik"), last_name=request.POST.get("Hanasi"))
    # count collection
    lclID = AddProducts.objects.count()
    status = "0"
    lclNewID = lclID + 1

    AddProducts.objects.create(
        ap_id=lclNewID,
        ap_category=request.POST["selCategory"],
        # ap_sub_category =request.POST["selSubCategory"],
        ap_name=request.POST["txtName"],
        ap_price=request.POST["txtPrice"],
        ap_quantity=request.POST["txtQuantity"],
        ap_image=request.FILES["txtImage"],
        ap_description=request.POST["txtDescription"],
        ap_status=status,
        ap_role=request.session["role"],
        ap_created_by=request.session["email"],
        ap_created_name=request.session["name"],
    )

    return HttpResponse()


def updateProduct(request):
    AddProducts.objects.filter(ap_id=request.POST["id"]).update(
        ap_category=request.POST["selCategory1"],
        ap_name=request.POST["txtName1"],
        ap_price=request.POST["txtPrice1"],
        ap_quantity=request.POST["txtQuantity1"],
        ap_description=request.POST["txtDescription1"],
    )
    return HttpResponse()
    # pass


def deleteProduct(request):
    AddProducts.objects.filter(ap_id=request.POST["id"]).update(ap_status="1")
    return HttpResponse()


def getProductData(request):
    if request.session["role"] == "Admin":
        products_json = AddProducts.objects.filter(ap_status="0").values()
        data = list(products_json)
        value = JsonResponse(data, safe=False)
        return value
    else:
        # print(request.session['email'])
        products_json = AddProducts.objects.filter(
            ap_status="0", ap_created_by=request.session["email"]
        ).values()
        data = list(products_json)
        value = JsonResponse(data, safe=False)
        return value


# def getSubCategory(request):

# 	subCategory_json = SubCategory.objects.filter(sc_status='0',sc_category= request.POST['selCategory']).values()
# 	data = list(subCategory_json)
# 	value = JsonResponse(data, safe=False)
# 	return value


def webGetCategories(request):
    category_json = Category.objects.filter(ca_status="0").values()
    data = list(category_json)
    value = JsonResponse(data, safe=False)
    return value


def getCategoryDetails(request):
    category_json = AddProducts.objects.filter(
        ap_status=0, ap_category=request.POST["txtID"]
    ).values()
    data = list(category_json)
    value = JsonResponse(data, safe=False)
    return value


def forgot_password(request):
    return render(request, "web/forgot_password.html", {})


def admin_forgot_password(request):
    return render(request, "admin/admin_forgot_password.html", {})


def updatePassword(request):
    return render(request, "web/update_password.html", {})


def adminUpdatePassword(request):
    return render(request, "admin/admin_update_password.html", {})


def forgotPassword(request):
    if ForgotPassword.objects.filter(fp_email=request.POST["txtEmail"]).count():
        ForgotPassword.objects.filter(fp_email=request.POST["txtEmail"]).update(
            fp_otp=request.POST["txtOTP"]
        )
    else:
        ForgotPassword.objects.create(
            fp_email=request.POST["txtEmail"], fp_otp=request.POST["txtOTP"]
        )
    send_mail(
        "OTP",
        "Your OTP is " + request.POST["txtOTP"],
        settings.EMAIL_HOST_USER,
        [request.POST["txtEmail"]],
        fail_silently=False,
    )
    return HttpResponse(0)


def adminForgotPassword(request):
    if ForgotPassword.objects.filter(fp_email=request.POST["txtEmail"]).count():
        ForgotPassword.objects.filter(fp_email=request.POST["txtEmail"]).update(
            fp_otp=request.POST["txtOTP"]
        )
    else:
        ForgotPassword.objects.create(
            fp_email=request.POST["txtEmail"], fp_otp=request.POST["txtOTP"]
        )
    send_mail(
        "OTP",
        "Your OTP is " + request.POST["txtOTP"],
        settings.EMAIL_HOST_USER,
        [request.POST["txtEmail"]],
        fail_silently=False,
    )
    return HttpResponse(0)


def validateOTP(request):
    if ForgotPassword.objects.filter(
        fp_email=request.POST["txtEmail"], fp_otp=request.POST["txtOTP"]
    ).count():
        request.session["forgot_email"] = request.POST["txtEmail"]
        return HttpResponse(0)
    else:
        return HttpResponse(10)


def updatePasswordValidate(request):
    Register.objects.filter(rg_email=request.session["forgot_email"]).update(
        rg_password=request.POST["txtPassword"]
    )
    return HttpResponse(0)


def adminUpdatePasswordValidate(request):
    AdminMaster.objects.filter(ad_email=request.session["forgot_email"]).update(
        ad_password=request.POST["txtPassword"]
    )
    return HttpResponse(0)


def userLogout(request):
    request.session.delete()
    return render(request, "web/index.html")


def getMyProfile(request):
    if "web_email" in request.session:
        jsonData = Register.objects.filter(
            rg_email=request.session["web_email"]
        ).values()
        data = list(jsonData)
        value = JsonResponse(data, safe=False)
        return value
    else:
        return 0
