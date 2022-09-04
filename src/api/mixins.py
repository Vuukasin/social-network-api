from rest_framework import permissions




class UserQuerySetMixin():
    user_field = "user"
    
    def get_queryset(self, *args, **kwargs):
        user = self.request.user
        lookup_data = {}
        lookup_data[self.user_field] = user
        qs = super().get_queryset(*args, **kwargs)
        return qs.filter(**lookup_data)
