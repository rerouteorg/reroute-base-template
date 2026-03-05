"""
Hello Route

This route handles /hello endpoints.

For path parameters (e.g., /users/{id}), create a subfolder named [id]:
    routes/users/[id]/page.py  ->  /users/{id}  (RECOMMENDED - Next.js style)
    routes/users/_id/page.py  ->  /users/{id}  (Alternative - for private routes)
    Use `from fastapi import Path` for path parameter injection.
"""

from fastapi import Query, Body, Path
from reroute import RouteBase
from reroute.decorators import rate_limit, cache
# noinspection PyUnresolvedReferences
from logger import get_logger

# Initialize logger for this module
logger = get_logger(__name__)


class HelloRoutes(RouteBase):
    """
    HelloRoutes handles /hello endpoints.

    Available methods:
    - GET: Retrieve hello
    - POST: Create new hello
    - PUT: Update hello
    - DELETE: Delete hello

    For individual item operations with path parameters:
    - Create a [id] subfolder (e.g., routes/users/[id]/page.py) - RECOMMENDED (Next.js style)
    - Or use _id subfolder (e.g., routes/users/_id/page.py) - for private/explicit routes
    - The [id] or _id folder becomes {id} in the URL path
    - Use `id: int = Path(...)` to extract the path parameter
    """

    # Swagger category/tag (optional - defaults to folder name)
    tag = "Hello"

    def __init__(self):
        super().__init__()
        # Initialize your data, database connections, etc.
        self.data = {}

    def before_request(self):
        """
        Hook that runs before every request.

        Use this for:
        - Authentication checks
        - Request validation
        - Logging

        Return a dict to short-circuit and return that response.
        Return None to continue to the handler.
        """
        pass

    @cache(duration=60)  # Cache for 60 seconds
    def get(self):
        """Handle GET requests - retrieve hello"""
        logger.info(f"GET request to /hello")
        return {
            "message": "GET /hello",
            "data": self.data
        }

    @rate_limit("10/min")  # Max 10 requests per minute
    def post(self):
        """Handle POST requests - create new hello"""
        # TODO: Implement POST logic
        return {
            "message": "POST /hello",
            "status": "created"
        }

    def put(self):
        """Handle PUT requests - update hello"""
        # TODO: Implement PUT logic
        return {
            "message": "PUT /hello",
            "status": "updated"
        }

    def patch(self):
        """Handle PATCH requests - partially update hello"""
        # TODO: Implement PATCH logic
        return {
            "message": "PATCH /hello",
            "status": "patched"
        }

    def delete(self):
        """Handle DELETE requests - delete hello"""
        # TODO: Implement DELETE logic
        return {
            "message": "DELETE /hello",
            "status": "deleted"
        }

    def after_request(self, response):
        """
        Hook that runs after every successful request.

        Args:
            response: The response dict from the handler

        Returns:
            Modified response dict
        """
        # Add custom headers, modify response, etc.
        return response

    def on_error(self, error: Exception):
        """
        Hook that runs when an error occurs.

        Args:
            error: The exception that occurred

        Returns:
            Error response dict (sanitized for security)
        """
        # Check if debug mode is enabled
        from config import AppConfig

        if AppConfig.DEBUG:
            return {
                "error": str(error),
                "type": type(error).__name__,
                "route": "/hello"
            }
        else:
            return {
                "error": "Internal server error",
                "type": "ServerError"
            }
