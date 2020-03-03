class Group:
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """Return True if user is in the group, False otherwise
    Arguments:
        user {str} -- User to lookup
        group {Group} -- Active directory group to look in

    Returns:
        [boolean] -- True if user in group False otherwise
    """

    if not isinstance(user, str):
        raise ValueError("Invalid user type. Must be string")
    elif not isinstance(group, Group):
        raise ValueError("Invalid group type. Must be Group object")

    def recursive_check_users(user, group):

        if user in group.users:
            return True

        if group.groups != []:  # Check for sub groups
            for g in group.groups:
                return recursive_check_users(user, g)
        else:
            return False

    return recursive_check_users(user, group)


if __name__ == "__main__":
    parent = Group("parent")
    child = Group("child")
    parent.add_group(child)
    sub_child = Group("subchild")
    child.add_group(sub_child)
    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)
    print(is_user_in_group("sub_child_user", parent))
    # Expected output: True
    print(is_user_in_group("Matt", parent))
    # Expected output: False
    print(is_user_in_group(None, parent))
    # Expect output: ValueError for wrong user type
