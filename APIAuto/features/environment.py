import requests

from utilities.configurations import getconfig
from utilities.recources import ApiResources


def after_scenario(context, scenario):
    if "lib" in scenario.tags:
        config = getconfig()
        url = config['API']['endpoint'] + ApiResources.deletebook
        resp = requests.post(url, json={"ID": context.id})
        print(resp.text)
