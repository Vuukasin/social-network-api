from rest_framework import permissions




class IsOwnerOrPostOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        if request.method == 'DELETE' and obj.post.user.id == request.user.id:
            return True

        return obj.user.id == request.user.id