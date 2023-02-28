class ImproperlyConfigured(Exception):
    """Raises when a environment variable is missing."""

    def __init__(self, variable_name: str, *args, **kwargs):
        self.variable_name = variable_name
        self.message = f"Set the {variable_name} environment variable."
        super().__init__(self.message, *args, **kwargs)


class NoSuchResource(Exception):
    """Raises when `RecourceManager` is a missing given resource."""

    def __init__(self, resource_name: str, *args, **kwargs):
        self.resource_name = resource_name
        self.message = f"Resource with name {resource_name} is missing."
        super().__init__(self.message, *args, **kwargs)


class UserAlreadyExists(Exception):
    """Raises when attempts to create a user with existing in the db user id."""

    def __init__(self, id: int, *args, **kwargs):
        self.user_id = id
        self.message = f"User with id {id} is already exists in the database."
        super().__init__(self.message, *args, **kwargs)


class UserDoesNotExists(Exception):
    """Raises when attempts to get a user with non-existing in the db user id."""

    def __init__(self, id: int, *args, **kwargs):
        self.user_id = id
        self.message = f"User with id {id} doesn't exists in the database."
        super().__init__(self.message, *args, **kwargs)


class CalculationError(Exception):
    """Raises when `TestResult` can't calculate test result."""

    pass
