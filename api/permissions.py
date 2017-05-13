from rest_framework.permissions import BasePermission, SAFE_METHODS
 
class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        # Permission for READ only request
        if request.method in SAFE_METHODS and request.user.is_authenticated():
            return True
        # Permission for WRITE only request
        else:
            return request.user.is_staff