from django.contrib import admin

from .models import (
    UserProfile,
    Address,
    Category,
    Product,
    Cart,
    CartItem,
    Order,
    OrderItem,
    Payment,
)


# ============================================================
# USER PROFILE
# ============================================================

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "user",
        "phone",
        "date_of_birth",
        "gender",
        "profile_image",
        "created_at",
        "updated_at",
    )

    search_fields = (
        "user__username",
        "user__first_name",
        "user__last_name",
        "user__email",
        "phone",
        "gender",
    )

    list_filter = (
        "gender",
        "created_at",
        "updated_at",
    )

    autocomplete_fields = (
        "user",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    ordering = (
        "-created_at",
    )

    list_per_page = 25


# ============================================================
# ADDRESS
# ============================================================

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "user",
        "name",
        "phone",
        "address_line1",
        "address_line2",
        "city",
        "state",
        "country",
        "pincode",
        "is_default",
        "created_at",
        "updated_at",
    )

    search_fields = (
        "user__username",
        "user__email",
        "name",
        "phone",
        "address_line1",
        "address_line2",
        "city",
        "state",
        "country",
        "pincode",
    )

    list_filter = (
        "is_default",
        "country",
        "state",
        "city",
        "created_at",
        "updated_at",
    )

    autocomplete_fields = (
        "user",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    ordering = (
        "-created_at",
    )

    list_per_page = 25


# ============================================================
# CATEGORY
# ============================================================

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "description",
        "is_active",
        "created_at",
        "updated_at",
    )

    search_fields = (
        "name",
        "description",
    )

    list_filter = (
        "is_active",
        "created_at",
        "updated_at",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    ordering = (
        "name",
    )

    list_per_page = 25


# ============================================================
# PRODUCT
# ============================================================

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "category",
        "price",
        "image",
        "is_active",
        "created_at",
        "updated_at",
    )

    search_fields = (
        "name",
        "description",
        "category__name",
    )

    list_filter = (
        "category",
        "is_active",
        "created_at",
        "updated_at",
    )

    autocomplete_fields = (
        "category",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    ordering = (
        "-created_at",
    )

    list_per_page = 25


# ============================================================
# CART
# ============================================================

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "user",
        "created_at",
        "updated_at",
    )

    search_fields = (
        "user__username",
        "user__email",
        "user__first_name",
        "user__last_name",
    )

    list_filter = (
        "created_at",
        "updated_at",
    )

    autocomplete_fields = (
        "user",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    ordering = (
        "-created_at",
    )

    list_per_page = 25


# ============================================================
# CART ITEM
# ============================================================

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "cart",
        "product",
        "quantity",
        "price",
        "total_price_display",
        "created_at",
        "updated_at",
    )

    search_fields = (
        "cart__user__username",
        "cart__user__email",
        "product__name",
    )

    list_filter = (
        "created_at",
        "updated_at",
    )

    autocomplete_fields = (
        "cart",
        "product",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
        "total_price_display",
    )

    ordering = (
        "-created_at",
    )

    list_per_page = 25

    @admin.display(description="Total Price")
    def total_price_display(self, obj):
        return obj.total_price


# ============================================================
# ORDER
# ============================================================

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "order_number",
        "user",
        "address",
        "subtotal",
        "discount",
        "shipping_charge",
        "total_amount",
        "payment_status",
        "order_status",
        "created_at",
        "updated_at",
    )

    search_fields = (
        "order_number",
        "user__username",
        "user__email",
        "user__first_name",
        "user__last_name",
        "address__name",
        "address__phone",
        "address__city",
        "address__pincode",
    )

    list_filter = (
        "payment_status",
        "order_status",
        "created_at",
        "updated_at",
    )

    autocomplete_fields = (
        "user",
        "address",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    ordering = (
        "-created_at",
    )

    list_per_page = 25


# ============================================================
# ORDER ITEM
# ============================================================

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "order",
        "product",
        "product_name",
        "quantity",
        "unit_price",
        "discount",
        "tax",
        "total_price",
        "created_at",
    )

    search_fields = (
        "order__order_number",
        "order__user__username",
        "order__user__email",
        "product__name",
        "product_name",
    )

    list_filter = (
        "created_at",
        "product",
    )

    autocomplete_fields = (
        "order",
        "product",
    )

    readonly_fields = (
        "created_at",
    )

    ordering = (
        "-created_at",
    )

    list_per_page = 25


# ============================================================
# PAYMENT
# ============================================================

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "order",
        "user",
        "payment_method",
        "gateway_order_id",
        "transaction_id",
        "amount",
        "currency",
        "status",
        "paid_at",
        "created_at",
        "updated_at",
    )

    search_fields = (
        "order__order_number",
        "user__username",
        "user__email",
        "gateway_order_id",
        "transaction_id",
        "payment_method",
        "currency",
    )

    list_filter = (
        "payment_method",
        "status",
        "currency",
        "paid_at",
        "created_at",
        "updated_at",
    )

    autocomplete_fields = (
        "order",
        "user",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    ordering = (
        "-created_at",
    )

    list_per_page = 25