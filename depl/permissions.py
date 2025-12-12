from rest_framework.permissions import BasePermission, SAFE_METHODS

class CanCreateSite(BasePermission):
    """
    List (GET) allowed for all authenticated users.
    Create (POST) allowed only for staff OR paid users.
    """

    message = "You must be staff or a paid user to create new Site entries."

    def has_permission(self, request, view):

        # Anyone authenticated can LIST
        if request.method in SAFE_METHODS:   # GET, HEAD, OPTIONS
            return request.user and request.user.is_authenticated

        # For CREATE -> check staff OR paid user
        return (
            request.user 
            and request.user.is_authenticated
            and (request.user.is_staff or getattr(request.user, "is_paid", False))
        )
