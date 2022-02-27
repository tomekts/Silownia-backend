from locust import HttpUser, task, between


class WebsiteTestUser(HttpUser):
    wait_time = between(0.1, 0.2)
    # patch="https://192.168.1.127:8888/"
    patch = "https://tomekts.pythonanywhere.com/"
    jw = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyNCwidXNlcm5hbWUiOiJ0b21hc3oiLCJleHAiOjE2MzY0NjAwMTUsImVtYWlsIjoiYWRtaW5Ad3AucGwifQ.5hamu_KVDktGXGMMlynfN2ZTIEouxxEkTYcoigz-5Ag"

    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        pass

    def on_stop(self):
        """ on_stop is called when the TaskSet is stopping """
        pass

    @task(1)
    def Check_home(self):
        self.client.get(self.patch, verify=False, )

    @task(1)
    def Check_login(self):
        headers = {"JW1": self.jw}
        self.client.post(self.patch+"check/", verify=False, cookies=headers)

    @task(1)
    def Save_series_in_database(self):
        headers = {"JW1": self.jw}
        date ={
                "id": 1,
                 "weight": 50,
                 "count": 10,
                "TrainingExercisesId": 3,
                "TrainingId": 7
                }
        self.client.put(self.patch+"rest/series/1/", verify=False, cookies=headers, data=date)

    @task(1)
    def Database_read_exercise(self):
        self.client.get(self.patch+"rest/exercises/", verify=False,)





