import time

from ...devices.device import BaseDevice
from ...utils import seed_everything
from .withings_authenticate import *
from .withings_extract import *

class_name = "ScanWatch"


class ScanWatch(BaseDevice):
    def __init__(self):
        self._authenticated = False
        self.valid_data_types = ["measurements"]

    def _default_params(self):
        return {"start": "2022-03-01", "end": "2022-06-17"}

    def _get_data(self, data_type, params):
        if data_type == "heart_rates":
            return fetch_all_heart_rate(
                self.access_token, params["start"], params["end"]
            )
        elif data_type == "sleeps":
            return fetch_all_sleeps(self.access_token, params["start"], params["end"])

    def _gen_synthetic(self, seed=0):
        # generate random data according to seed
        seed_everything(seed)

        self.measurements = []

        # load in the CSV that we've pre-generated
        # df = pd.read_csv("random_data.csv")
        # fix dates, convert to datetime obj from string
        # df.date = df.date.apply(lambda x: datetime.strptime(x, "%Y-%m-%d %H:%M:%S.%f"))

        # df = df[[col for col in df.columns if "Unnamed: 0" not in col]]

        # return df

    def authenticate(self, auth_creds):
        # authenticate this device against API

        self.auth_creds = auth_creds

        self.access_token = withings_authenticate(auth_creds)
        self._authenticated = True

        self.auth_creds = auth_creds
