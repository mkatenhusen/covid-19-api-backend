from rest_framework.viewsets import GenericViewSet


class MixedPermissionsViewSetMixin(GenericViewSet):
    permission_classes_by_action: dict

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]
