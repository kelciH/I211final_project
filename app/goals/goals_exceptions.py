# Author: Kelci Kempson
# Date: 11/12/26
# File: goals_exceptions.py
# Description: goal exceptions

class GoalException(Exception):
    # Base exception class for movie-specific exceptions
    pass

class GoalNotFoundException(GoalException):
    # Exception raised when a movie is not found in the database
    pass
