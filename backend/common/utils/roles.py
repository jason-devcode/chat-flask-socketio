from functools import reduce

from common.constants.roles import RoleBitPosition


def get_role_bitmask(role: RoleBitPosition) -> int:
    """
    Returns the bitmask for a single role.

    Args:
        role (RoleBitPosition): The role whose bitmask should be retrieved.

    Returns:
        int: The bitmask with only the specified role bit set.
    """
    return 1 << role.value


def get_combined_roles_bitmask(roles: list[RoleBitPosition]) -> int:
    """
    Returns a combined bitmask for multiple roles.

    Args:
        roles (list[RoleBitPosition]): A list of roles to combine into a single bitmask.

    Returns:
        int: The combined bitmask with all specified role bits set.
    """
    return reduce(lambda mask, role: mask | (1 << role.value), roles, 0)


def has_roles_in_bitmask(user_bitmask: int, roles: list[RoleBitPosition]) -> bool:
    """
    Checks if the given user bitmask contains all the specified roles.

    Args:
        user_bitmask (int): The bitmask representing the user's roles.
        roles (list[RoleBitPosition]): A list of roles to check within the bitmask.

    Returns:
        bool: True if all specified roles are present in the user's bitmask, False otherwise.
    """
    required_mask = get_combined_roles_bitmask(roles)
    return (user_bitmask & required_mask) == required_mask
