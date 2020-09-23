from django.contrib.auth.models import Group, Permission
from django.core.management.base import BaseCommand

from apps.users.models import User


class Command(BaseCommand):
    GROUPS = {
        User.VISITORS_GROUP_NAME: (
        ),
        User.ADMINISTRATORS_GROUP_NAME: (
        ),
    }

    def handle(self, *args, **options):
        for group_name, group_permissions in self.GROUPS.items():
            new_group, created = Group.objects.get_or_create(name=group_name)

            for permission_name in group_permissions:
                try:
                    model_add_perm = Permission.objects.get(codename=permission_name)
                except Permission.DoesNotExist:
                    print(f'Permission "{permission_name}" not found')
                    continue

                new_group.permissions.add(model_add_perm)
                print(f'Permission "{permission_name}" added to group {group_name}')
