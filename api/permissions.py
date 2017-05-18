from rest_framework.permissions import BasePermission, SAFE_METHODS
 
class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        # Permission for READ only request
        if request.method in SAFE_METHODS and request.user.is_authenticated():
            return True
        # Permission for WRITE only request
        else:
            return request.user.is_staff

class IsUserAndReadAndCreate(BasePermission):
    def has_object_permission(self, request, view, obj):
        # If user is logged in
        if request.user.is_authenticated():
            # Permission for READ only request
            if request.method in SAFE_METHODS:
                return True
            # Permission for POST as well
            if request.method == "POST":
                return True
        return False

class IsGameCreator(BasePermission):
    def has_object_permission(self, request, view, obj):
        # If user is logged in
        if request.user.is_authenticated():
            # Permission for READ only request
            if request.method in SAFE_METHODS:
                return True
            # If the user created the game
            if obj.gameOrganizer.id == request.user.id:
                return True
        return False

class IsGameUserCreator(BasePermission):
    def has_object_permission(self, request, view, obj):
        # If user is logged in
        if request.user.is_authenticated():
            # Permission for READ only request
            if request.method in SAFE_METHODS:
                return True
            # If the user joined the game
            if obj.user.id == request.user.id:
                return True
        return False