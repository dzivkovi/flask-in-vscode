"""
This module contains the business logic for a Flask application that serves as a greeting service.
It includes a function to create a personalized greeting using a provided name.

Note:
- Business logic goes in here
- To start VSCode Flask debugger make sure to be in the app.py file
- To start Flask app from the command line, run:
    python -m flask run --port 5000
"""

from datetime import datetime
import re

def greeting(name):
    """
    Generate a personalized greeting with the provided name and current timestamp.
    If the name contains any characters that are not letters, the greeting will use "Friend".

    Args:
        name (str): Name of the person to be greeted. 

    Returns:
        str: A personalized greeting string with current date and time.
    """

    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    # Filter the name argument to letters only using regular expressions. URL arguments
    # can contain arbitrary text, so we restrict to safe characters only.
    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    content = "Hello there, " + clean_name + "! It's " + formatted_now
    return content

# Main function to quickly test the business logic
if __name__=='__main__':
    FIRSTNAME = "Don@van"
    print("Input : " + FIRSTNAME + "\nOutput: " + greeting(FIRSTNAME))
