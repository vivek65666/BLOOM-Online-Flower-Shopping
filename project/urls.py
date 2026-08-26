"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views


urlpatterns = [
    # path('admin/', admin.site.urls),
    path("", views.openHome),
    path("index/", views.openHome),
    path("about/", views.viewAbout),
    path("shop/", views.viewShop),
    path("gallery/", views.viewGalley),
    path("contact/", views.viewContact),
    path("login/", views.viewLogin),
    path("register/", views.viewRegister),
    path("cart/", views.viewCart),
    path("checkout/", views.viewCheckOut),
    # admin
    path("add_admin/", views.adminAdd_admin),
    path("add_vendor/", views.adminAdd_vendor),
    path("auth-normal-sign-in/", views.adminSignin),
    path("index_admin/", views.adminIndex),
    path("view_orders/", views.adminOrders),
    path("view_payment/", views.adminPayment),
    path("view_product/", views.adminProduct),
    path("view_users/", views.adminUsers),
    path("admin_master/", views.adminAdmin),
    path("profile/", views.adminProfile),
    path("vendor_profile/", views.vendor_profile),
    path("web_profile/", views.web_profile),
    path("get_profile_data/", views.adminProfileData),
    path("get_user_profile_data/", views.userProfileData),
    path("admin_update_profile/", views.adminUpdateProfileData),
    path("update_user_profile/", views.updateUserProfile),
    path("add_product/", views.addProduct),
    path("admin_login/", views.adminLogin),
    # admin database
    path("addAdmin_Master/", views.viewAdminMaster),
    # path('addOrganic_Products/',views.viewOrganicProducts),
    path("check_admin_login/", views.checkAdminLogin, name="admin_login"),
    path("check_web_login/", views.checkWebLogin, name="web_login"),
    path("user_logout/", views.userLogout, name="user_logout"),
    path("get_product_details/", views.getProductDetails, name="web_login"),
    path("get_single_item/", views.getSingleItem, name="web_login"),
    path("get_user_data/", views.getUserData, name="web_login"),
    path("get_order_data/", views.getOrderData, name="web_login"),
    path("add_cart/", views.addCart, name="cart"),
    path("get_cart/", views.getCart, name="cart"),
    path("checkout/payment/", views.checkoutPayment, name="payment"),
    path("check_checkout/", views.checkCheckout, name="payment"),
    path("get_buy_now_url/", views.getBuyNowURL, name="payment"),
    path("order_history/", views.viewOrderHistory),
    path("get_order_history/", views.getOrderHistory, name="payment"),
    path("add_register/", views.newRegister, name="home"),
    path("cancel_item/", views.cancelItem, name="home"),
    path("pay_success/", views.paymentSuccess, name="payment"),
    #   Vendor
    path("vendor_index/", views.viewVendorIndex),
    path("vendor_users/", views.viewUsers),
    path("viewvendor_orders/", views.viewVendorOrders),
    path("get_cart_count/", views.viewCartCount),
    # path('add_Products/',views.viewVendorProduct),
    path("shop-details/", views.viewShopDetails),
    path("product-single/", views.viewSingleProduct),
    path("categories/", views.viewCategories, name="categories"),
    path("add/category/", views.addCategory, name="category"),
    path("update/category/", views.updateCategory, name="category"),
    path("delete/category/", views.deleteCategory, name="category"),
    path("get_data/category/", views.getCategoryData, name="category"),
    # path('sub_categories/', views.subCategories, name='sub_categories'),
    # path('add/sub_category/', views.addSubCategory, name='sub_category'),
    # path('update/sub_category/', views.updateSubCategory, name='category'),
    # path('delete/sub_category/', views.deleteSubCategory, name='category'),
    # path('get_data/sub_category/', views.getSubCategoryData, name='category'),
    path("vendor_product/", views.viewAddProduct),
    path("add/product/", views.viewVendorProduct, name="product"),
    path("update/product/", views.updateProduct, name="product"),
    path("delete/product/", views.deleteProduct, name="product"),
    path("get_data/product/", views.getProductData, name="product"),
    path("get_my_profile/", views.getMyProfile, name="product"),
    path("web_get_categories/", views.webGetCategories, name="get_category_web_data"),
    path("category_detail/", views.getcategoryDetails, name="product"),
    path(
        "get_category_details/", views.getCategoryDetails, name="get_category_web_data"
    ),
    path("forgot_password/", views.forgot_password),
    path("admin_forgot_password/", views.admin_forgot_password),
    path("forgot_password_otp/", views.forgotPassword),
    path("admin_forgot_password_otp/", views.adminForgotPassword),
    path("validate_otp/", views.validateOTP),
    path("update_password/", views.updatePassword),
    path("admin_update_password/", views.adminUpdatePassword),
    path("update_password_validate/", views.updatePasswordValidate),
    path("admin_update_password_validate/", views.adminUpdatePasswordValidate),
]
