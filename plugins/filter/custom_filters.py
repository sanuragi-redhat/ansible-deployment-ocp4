# plugins/filter/custom_filters.py
from ansible.errors import AnsibleFilterError

def upper_case(value):
    """Convert a string to uppercase."""
    if not isinstance(value, str):
        raise AnsibleFilterError("upper_case filter requires a string input")
    return value.upper()

class FilterModule(object):
    """Custom Jinja2 filters."""
    def filters(self):
        return {
            'upper_case': upper_case
        }
