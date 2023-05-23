import requests
import json


def get_user_activity_calls(refresh_token, account_key, client_id, client_secret):
    """
    Gets the user activity calls for the specified account.

    Args:
        refresh_token: The refresh token for the account.
        account_key: The account key for the account.
        client_id: The client ID for the application.
        client_secret: The client secret for the application.

    Returns:
        A list of user activity calls.
    """

    # Create the request URL.
    url = "https://api.jive.com/call-reports/v1/reports/user-activity".format(account_key)

    # Create the request headers.
    headers = {
        "Authorization": "Bearer {}".format(refresh_token),
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

    # Make the request.
    response = requests.get(url, headers=headers)

    # Check the response status code.
    if response.status_code != 200:
        raise Exception("Error getting user activity calls: {}".format(response.status_code))

    # Get the response data.
    response_data = response.json()

    # Return the user activity calls.
    return response_data["calls"]


if __name__ == "__main__":
    # Get the refresh token, account key, client ID, and client secret.
    refresh_token = "eyJraWQiOiI2MjAiLCJhbGciOiJSUzUxMiJ9.eyJzYyI6ImNhbGwtY29udHJvbC52MS5jYWxscy5jb250cm9sIGNhbGxzLnYyLmluaXRpYXRlIG1lc3NhZ2luZy52MS53cml0ZSBpZGVudGl0eTpzY2ltLm1lIGNhbGwtZXZlbnRzLnYxLmV2ZW50cy5yZWFkIG1lc3NhZ2luZy52MS5ub3RpZmljYXRpb25zLm1hbmFnZSB2b2ljZW1haWwudjEubm90aWZpY2F0aW9ucy5tYW5hZ2Ugc3VwcG9ydDogdm9pY2VtYWlsLnYxLnZvaWNlbWFpbHMud3JpdGUgZmF4LnYxLndyaXRlIHZvaWNlLWFkbWluLnYxLndyaXRlIGlkZW50aXR5OiB3ZWJydGMudjEucmVhZCB3ZWJydGMudjEud3JpdGUgY29sbGFiOiB2b2ljZS1hZG1pbi52MS5yZWFkIHByZXNlbmNlLnYxLnJlYWQgY2FsbC1ldmVudHMudjEubm90aWZpY2F0aW9ucy5tYW5hZ2UgaWRlbnRpdHk6c2NpbS5vcmcgcHJlc2VuY2UudjEud3JpdGUgZmF4LnYxLnJlYWQgY2FsbC1oaXN0b3J5LnYxLm5vdGlmaWNhdGlvbnMubWFuYWdlIHByZXNlbmNlLnYxLm5vdGlmaWNhdGlvbnMubWFuYWdlIG1lc3NhZ2luZy52MS5zZW5kIG1lc3NhZ2luZy52MS5yZWFkIGNyLnYxLnJlYWQgZmF4LnYxLm5vdGlmaWNhdGlvbnMubWFuYWdlIHVzZXJzLnYxLmxpbmVzLnJlYWQgdm9pY2VtYWlsLnYxLnZvaWNlbWFpbHMucmVhZCIsInN1YiI6IjE4OTQ1NzIxODU1Mjg3NDEzODIiLCJhdWQiOiIxYmU3YTRmMC0wNTYwLTQ5NDUtOTcxOS0yMjI3ODJkYjAzN2YiLCJvZ24iOiJwd2QiLCJ0eXAiOiJyIiwiZXhwIjoxNjgzNzE2NDk3LCJpYXQiOjE2ODExMjQ0OTcsImp0aSI6IjU4NDNmNzhkLTdkNjUtNDRhZi1iNDkwLWFlZTY1OWE1ODkzNiJ9.yV3emzEc4s19HsBdjmFFBh3ScWtSXD_xkbyHIWRg9-RPwFXn4-ihHrmH1C8IMaqmY0z-6HpSRwXt9AXa8tcjm5tyfspMx0P4wUGb1HFUdCxjJpVAY5XtO-zWhQFWwQnjHLA7xcNAjMrdNchKiT69d9KZR1QFQUCIgSf6Jg4PghdsX5iRS5rf77zWiSZ6U111vMa3SWjzmSmSyQ3tO4dc6abEbmOVFZ7H0I2gd22pJ_oHNbIwZSMWQ2rBrFx4BEzwUMn46YcHb2dmfGaDk-dfqBpOIKswDiaSj1tZhiGh1GpcDE10DXpjslF77ZoD1FExruH8g9V96ecTzAa32bZoqg"
    account_key = "2931278622294264462"
    client_id = "1be7a4f0-0560-4945-9719-222782db037f"
    client_secret = "BvnlNB5ePIndDtxPjncXm4DW"

    # Get the user activity calls.
    calls = get_user_activity_calls(refresh_token, account_key, client_id, client_secret)

    # Print the user activity calls.
    for call in calls:
        print(call)