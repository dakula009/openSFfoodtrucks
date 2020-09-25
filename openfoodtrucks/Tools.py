import datetime

class QueryMaker:
    """This class makes the Socrata query for the url request by using the current time
    """
    def __init__(self, page_num):
        self.datetime_now = datetime.datetime.now()
        self.page_num = page_num

    def make_query(self):
        # get hour and minute from datetime_now
        hour_now = self.datetime_now.hour
        minute_now = self.datetime_now.minute
        time_now = f'{hour_now}:{minute_now}'

        # get the number of day from datetime_now
        day_now = self.datetime_now.isoweekday()

        # limit per page is 10
        limit = 10

        # base url to use
        base_url = "http://data.sfgov.org/resource/bbb8-hzi6.json"

        # build a Socrata query according to the requriements, reference: https://dev.socrata.com/docs/queries/
        # offset = page_number * limit
        query = f"?$select=applicant, location&$where='{time_now}' BETWEEN start24 AND end24 " \
            f"AND dayorder={day_now}&$order=applicant ASC&$limit={limit}&$offset={self.page_num * limit}"

        # combine base_url and query
        query_url = base_url + query

        return query_url
