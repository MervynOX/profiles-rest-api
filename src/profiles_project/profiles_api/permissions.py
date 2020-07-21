# for Django REST framwork to decide whether a user has permission to manage the database

from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile."""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""

        # just view the profile
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id

class PostOwnStatus(permissions.BasePermission):
    """Allow user to updated their own status."""

    def has_object_permission(self, request, view, obj):
        """Check the user is trying to update their own status."""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id # check status id == to profile id

class UpdateOwnEvent(permissions.BasePermission):
    """Allow user to updated their own event."""

    def has_object_permission(self, request, view, obj):
        """Check the user is trying to update their own event."""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id # check status id == to profile id

class UpdateOwnCommunity(permissions.BasePermission):
    """Allow user to updated their own community."""

    def has_object_permission(self, request, view, obj):
        """Check the user is trying to update their own event."""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id
