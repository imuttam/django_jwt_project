from rest_framework.permissions import BasePermission

class IsPaidUser(BasePermission):
    message = "Upgrade to paid plan to modify this resource."

    def has_permission(self, request, view):
        # Allow all authenticated users to GET
        if request.method in ("GET", "HEAD", "OPTIONS"):
            return request.user and request.user.is_authenticated
        
        # Only paid users allowed for Create / Update / Delete
        return request.user and request.user.is_authenticated and request.user.is_paid
