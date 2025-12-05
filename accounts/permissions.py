# from rest_framework.permissions import BasePermission

# class IsPaidUser(BasePermission):
#     message = "Upgrade to paid plan to modify this resource."

#     def has_permission(self, request, view):
#         # Allow all authenticated users to GET
#         if request.method in ("GET", "HEAD", "OPTIONS"):
#             return request.user and request.user.is_authenticated
        
#         # Only paid users allowed for Create / Update / Delete
#         return request.user and request.user.is_authenticated and request.user.is_paid

## Final Way

from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdmin(BasePermission):
    """
    Allow access only to admin users (is_staff=True).
    """
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.is_staff)


class IsPaidUser(BasePermission):
    """
    - Allow all authenticated users to READ (GET, HEAD, OPTIONS).
    - Allow only paid users to WRITE (POST, PUT, PATCH, DELETE).
    """
    message = "Upgrade to paid plan to modify this resource."

    def has_permission(self, request, view):
        # Read-only methods
        if request.method in SAFE_METHODS:  # GET, HEAD, OPTIONS
            return bool(request.user and request.user.is_authenticated)

        # Write methods: only paid users
        return bool(
            request.user
            and request.user.is_authenticated
            and request.user.is_paid
        )


class IsAdminOrPaidUser(BasePermission):
    """
    Admins can do everything.
    Paid users can also do everything.
    Free users can only read.
    Anonymous cannot access at all.
    """
    message = "You must be admin or paid user to modify this resource."

    def has_permission(self, request, view):
        user = request.user

        # Must be authenticated for anything
        if not (user and user.is_authenticated):
            return False

        # Admin always allowed
        if user.is_staff:
            return True

        # Free vs Paid logic
        if request.method in SAFE_METHODS:
            return True  # free and paid can read

        # For write operations, only paid users
        return user.is_paid
