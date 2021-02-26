import json
import logging
import requests

REPO_HOSTNAME = "http://localhost:8081"
USER = 'LCpO0Lh8'
TOKEN = 'aSVxh5KRrDJbZ04NGqRrEgQyzR1mNh_byFz-BWQhpS73'
REPO = "<REPO NAME HERE>"

log = logging.getLogger('hasbrowns-order')


def main():
    logging.basicConfig(filename='./hashbrowns-order.log', level=logging.INFO)
    get_artifacts(REPO)


def get_artifacts(repo_name):
    response = requests.get('{0}/service/rest/v1/search/?sort=name&repository={1}'.format(
        REPO_HOSTNAME, repo_name),
        auth=(USER, TOKEN)
    )

    if response.ok:
        res = json.loads(response.text)
        # print("REPO NAME: {0} - {1}".format(repo_name, res))
        for artifact in res['items']:
            name = artifact['name']
            for asset in artifact['assets']:
                print("{0}  {1}".format(asset["checksum"]["sha1"], name))
    # Control entry
    print("070e02e901924a40097b847cff4066c15d3a684b  struts2-core-2.5.10.jar")


if __name__ == '__main__':
    main()
