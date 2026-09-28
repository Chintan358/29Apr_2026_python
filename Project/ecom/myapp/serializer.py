import uuid
from decimal import Decimal

from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.db import transaction
from rest_framework import serializers

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
# USER / AUTH
# ============================================================

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "first_name", "last_name"]
        read_only_fields = ["id"]


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, validators=[validate_password]
    )
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            "id", "username", "email", "first_name", "last_name",
            "password", "confirm_password",
        ]
        read_only_fields = ["id"]

    def validate_email(self, value):
        if User.objects.filter(email__iexact=value).exists():
            raise serializers.ValidationError("Email is already registered.")
        return value

    def validate(self, attrs):
        if attrs["password"] != attrs.pop("confirm_password"):
            raise serializers.ValidationError(
                {"confirm_password": "Passwords do not match."}
            )
        return attrs

    @transaction.atomic
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        UserProfile.objects.create(user=user)
        Cart.objects.create(user=user)
        return user


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(
        write_only=True, validators=[validate_password]
    )

    def validate_old_password(self, value):
        user = self.context["request"].user
        if not user.check_password(value):
            raise serializers.ValidationError("Old password is incorrect.")
        return value

    def save(self, **kwargs):
        user = self.context["request"].user
        user.set_password(self.validated_data["new_password"])
        user.save()
        return user


# ============================================================
# USER PROFILE
# ============================================================

class UserProfileSerializer(serializers.ModelSerializer):
    # Read-only nested user; editable user fields are accepted flat below
    user = UserSerializer(read_only=True)
    first_name = serializers.CharField(
        source="user.first_name", required=False, allow_blank=True
    )
    last_name = serializers.CharField(
        source="user.last_name", required=False, allow_blank=True
    )
    email = serializers.EmailField(source="user.email", required=False)

    class Meta:
        model = UserProfile
        fields = [
            "id", "user", "first_name", "last_name", "email",
            "phone", "date_of_birth", "gender", "profile_image",
            "created_at", "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]

    def update(self, instance, validated_data):
        user_data = validated_data.pop("user", {})
        if user_data:
            for attr, value in user_data.items():
                setattr(instance.user, attr, value)
            instance.user.save()
        return super().update(instance, validated_data)


# ============================================================
# ADDRESS
# ============================================================

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = [
            "id", "name", "phone", "address_line1", "address_line2",
            "city", "state", "country", "pincode", "is_default",
            "created_at", "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]

    def validate_pincode(self, value):
        if not value.isdigit() or len(value) != 6:
            raise serializers.ValidationError("Enter a valid 6-digit pincode.")
        return value

    def validate_phone(self, value):
        digits = value.replace("+", "").replace(" ", "").replace("-", "")
        if not digits.isdigit() or not (10 <= len(digits) <= 15):
            raise serializers.ValidationError("Enter a valid phone number.")
        return value

    def _unset_other_defaults(self, user, exclude_id=None):
        qs = Address.objects.filter(user=user, is_default=True)
        if exclude_id:
            qs = qs.exclude(pk=exclude_id)
        qs.update(is_default=False)

    @transaction.atomic
    def create(self, validated_data):
        user = self.context["request"].user
        validated_data["user"] = user
        # First address becomes default automatically
        if not Address.objects.filter(user=user).exists():
            validated_data["is_default"] = True
        if validated_data.get("is_default"):
            self._unset_other_defaults(user)
        return super().create(validated_data)

    @transaction.atomic
    def update(self, instance, validated_data):
        if validated_data.get("is_default"):
            self._unset_other_defaults(instance.user, exclude_id=instance.pk)
        return super().update(instance, validated_data)


# ============================================================
# CATEGORY
# ============================================================

class CategorySerializer(serializers.ModelSerializer):
    products_count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = [
            "id", "name", "description", "is_active", "products_count",
            "created_at", "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]

    def get_products_count(self, obj):
        # Use annotate(products_count=...) in the view to avoid N+1 queries
        return getattr(
            obj, "_products_count", obj.products.filter(is_active=True).count()
        )


# ============================================================
# PRODUCT
# ============================================================

class ProductListSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source="category.name", read_only=True)

    class Meta:
        model = Product
        fields = [
            "id", "category", "category_name", "name",
            "price", "image", "is_active",
        ]
        read_only_fields = ["id"]


class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source="category.name", read_only=True)

    class Meta:
        model = Product
        fields = [
            "id", "category", "category_name", "name", "description",
            "price", "image", "is_active", "created_at", "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price must be greater than 0.")
        return value

    def validate_category(self, value):
        if not value.is_active:
            raise serializers.ValidationError("Category is not active.")
        return value


# ============================================================
# CART
# ============================================================

class CartItemSerializer(serializers.ModelSerializer):
    product_detail = ProductListSerializer(source="product", read_only=True)
    total_price = serializers.DecimalField(
        max_digits=14, decimal_places=2, read_only=True
    )

    class Meta:
        model = CartItem
        fields = [
            "id", "product", "product_detail", "quantity",
            "price", "total_price", "created_at", "updated_at",
        ]
        # price is always taken from the product, never from the client
        read_only_fields = ["id", "price", "created_at", "updated_at"]

    def validate_product(self, value):
        if not value.is_active:
            raise serializers.ValidationError("This product is unavailable.")
        return value

    def validate_quantity(self, value):
        if value < 1:
            raise serializers.ValidationError("Quantity must be at least 1.")
        return value


class AddToCartSerializer(serializers.Serializer):
    """Adds a product to the cart; increments quantity if it already exists."""

    product = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.filter(is_active=True)
    )
    quantity = serializers.IntegerField(min_value=1, default=1)

    def save(self, **kwargs):
        cart, _ = Cart.objects.get_or_create(user=self.context["request"].user)
        product = self.validated_data["product"]
        quantity = self.validated_data["quantity"]

        item, created = CartItem.objects.get_or_create(
            cart=cart,
            product=product,
            defaults={"quantity": quantity, "price": product.price},
        )
        if not created:
            item.quantity += quantity
            item.price = product.price  # refresh to current price
            item.save()
        return item


class UpdateCartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ["quantity"]

    def validate_quantity(self, value):
        if value < 1:
            raise serializers.ValidationError("Quantity must be at least 1.")
        return value


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)
    total_items = serializers.SerializerMethodField()
    subtotal = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = [
            "id", "items", "total_items", "subtotal",
            "created_at", "updated_at",
        ]
        read_only_fields = fields

    def get_total_items(self, obj):
        return sum(item.quantity for item in obj.items.all())

    def get_subtotal(self, obj):
        return sum((item.total_price for item in obj.items.all()), Decimal("0.00"))


# ============================================================
# ORDER ITEM
# ============================================================

class OrderItemSerializer(serializers.ModelSerializer):
    product_image = serializers.ImageField(source="product.image", read_only=True)

    class Meta:
        model = OrderItem
        fields = [
            "id", "product", "product_name", "product_image", "quantity",
            "unit_price", "discount", "tax", "total_price", "created_at",
        ]
        read_only_fields = fields


# ============================================================
# PAYMENT
# ============================================================

class PaymentSerializer(serializers.ModelSerializer):
    order_number = serializers.CharField(source="order.order_number", read_only=True)

    class Meta:
        model = Payment
        fields = [
            "id", "order", "order_number", "payment_method",
            "gateway_order_id", "transaction_id", "amount", "currency",
            "status", "paid_at", "created_at", "updated_at",
        ]
        read_only_fields = [
            "id", "order", "gateway_order_id", "transaction_id", "amount",
            "currency", "status", "paid_at", "created_at", "updated_at",
        ]


class CreatePaymentSerializer(serializers.Serializer):
    """Initiates a payment for an existing order."""

    order = serializers.PrimaryKeyRelatedField(queryset=Order.objects.all())
    payment_method = serializers.ChoiceField(choices=Payment.PAYMENT_METHODS)

    def validate_order(self, order):
        user = self.context["request"].user
        if order.user_id != user.id:
            raise serializers.ValidationError("Order not found.")
        if order.payment_status == "PAID":
            raise serializers.ValidationError("Order is already paid.")
        if order.order_status in ("CANCELLED", "REFUNDED"):
            raise serializers.ValidationError("Order can no longer be paid.")
        return order

    def create(self, validated_data):
        order = validated_data["order"]
        return Payment.objects.create(
            order=order,
            user=order.user,
            payment_method=validated_data["payment_method"],
            amount=order.total_amount,
        )


class VerifyRazorpayPaymentSerializer(serializers.Serializer):
    """Payload sent by the client after Razorpay checkout succeeds.
    Signature verification itself should be done in the view/service."""

    razorpay_order_id = serializers.CharField()
    razorpay_payment_id = serializers.CharField()
    razorpay_signature = serializers.CharField()


# ============================================================
# ORDER
# ============================================================

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    payments = PaymentSerializer(many=True, read_only=True)
    address_detail = AddressSerializer(source="address", read_only=True)
    payment_status_display = serializers.CharField(
        source="get_payment_status_display", read_only=True
    )
    order_status_display = serializers.CharField(
        source="get_order_status_display", read_only=True
    )

    class Meta:
        model = Order
        fields = [
            "id", "order_number", "address", "address_detail",
            "subtotal", "discount", "shipping_charge", "total_amount",
            "payment_status", "payment_status_display",
            "order_status", "order_status_display",
            "items", "payments", "created_at", "updated_at",
        ]
        read_only_fields = fields


class OrderListSerializer(serializers.ModelSerializer):
    items_count = serializers.IntegerField(source="items.count", read_only=True)

    class Meta:
        model = Order
        fields = [
            "id", "order_number", "total_amount", "payment_status",
            "order_status", "items_count", "created_at",
        ]
        read_only_fields = fields


class CreateOrderSerializer(serializers.Serializer):
    """Creates an order from the user's current cart."""

    address = serializers.PrimaryKeyRelatedField(queryset=Address.objects.all())
    payment_method = serializers.ChoiceField(
        choices=Payment.PAYMENT_METHODS, required=False
    )

    def validate_address(self, address):
        if address.user_id != self.context["request"].user.id:
            raise serializers.ValidationError("Address not found.")
        return address

    @staticmethod
    def _generate_order_number():
        return f"ORD-{uuid.uuid4().hex[:10].upper()}"

    @transaction.atomic
    def create(self, validated_data):
        user = self.context["request"].user
        address = validated_data["address"]

        try:
            cart = Cart.objects.select_for_update().get(user=user)
        except Cart.DoesNotExist:
            raise serializers.ValidationError({"cart": "Cart is empty."})

        cart_items = list(cart.items.select_related("product"))
        if not cart_items:
            raise serializers.ValidationError({"cart": "Cart is empty."})

        inactive = [i.product.name for i in cart_items if not i.product.is_active]
        if inactive:
            raise serializers.ValidationError(
                {"cart": f"Unavailable products: {', '.join(inactive)}"}
            )

        # Always price from the current product price (server-side)
        subtotal = sum(
            (i.product.price * i.quantity for i in cart_items), Decimal("0.00")
        )
        discount = Decimal("0.00")
        shipping_charge = Decimal("0.00")  # plug in your shipping logic here
        total_amount = subtotal - discount + shipping_charge

        order = Order.objects.create(
            user=user,
            address=address,
            order_number=self._generate_order_number(),
            subtotal=subtotal,
            discount=discount,
            shipping_charge=shipping_charge,
            total_amount=total_amount,
        )

        OrderItem.objects.bulk_create([
            OrderItem(
                order=order,
                product=i.product,
                product_name=i.product.name,  # snapshot
                quantity=i.quantity,
                unit_price=i.product.price,    # snapshot
                total_price=i.product.price * i.quantity,
            )
            for i in cart_items
        ])

        payment_method = validated_data.get("payment_method")
        if payment_method:
            Payment.objects.create(
                order=order,
                user=user,
                payment_method=payment_method,
                amount=total_amount,
            )

        cart.items.all().delete()  # clear cart after order is placed
        return order

    def to_representation(self, instance):
        return OrderSerializer(instance, context=self.context).data


class UpdateOrderStatusSerializer(serializers.ModelSerializer):
    """For admin / staff use only."""

    class Meta:
        model = Order
        fields = ["order_status", "payment_status"]