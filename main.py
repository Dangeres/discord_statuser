import requests
import time
import json


def main():
    print('started')

    config_file = 'config.json'

    with open(config_file, 'r') as file_:
        config = json.loads(file_.read())

    statuses = config.get('statuses', [])
    channel_id = config.get('channel_id')
    token = config.get('token')

    while True:
        for status in statuses:
            response = requests.put(
                url = f"https://discord.com/api/v9/channels/{channel_id}/voice-status",
                json = {
                    'status': status,
                },
                headers = {
                    'Content-Type': 'application/json',
                    'Authorization': token,
                }
            )

            print(f'{status} - {response.status_code}')

            time.sleep(0.5)


if __name__ == '__main__':
    main()
