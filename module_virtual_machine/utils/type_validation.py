"""Validate parameter"""
class TypeValidation:
    """Class that has methods to validate the type of parameter."""

    def validate_string_param(self, param, param_name):
        """Validate the type of parameter."""
        if not isinstance(param, str):
            raise TypeError(f'The "{param_name}" parameter must be of type str.')
