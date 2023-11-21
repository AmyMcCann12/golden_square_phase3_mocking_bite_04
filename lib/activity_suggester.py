
class ActivitySuggester:
    def __init__(self, requester):
        self._requester = requester

    def suggest(self):
        response = self._make_request_to_api()
        return f"Why not: {response['activity']}"

    # This method calls an 'API' on the internet to get a random activity.
    # An API is a way of allowing programs to request data from other programs.
    def _make_request_to_api(self):
        response = self._requester.get("http://www.boredapi.com/api/activity")
        return response.json()

# Usage
# =====
import requests
activity_suggester = ActivitySuggester(requests)
# activity_suggester.suggest() will return a different value every time

print(activity_suggester.suggest())
# Why not: Learn how to use a french press

print(activity_suggester.suggest())
# Why not: Hold a video game tournament with some friends