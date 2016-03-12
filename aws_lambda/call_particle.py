import json
import urllib
import urllib2

repo_to_led = {}
repo_to_led['scala-playground'] = 1
repo_to_led['xmas-photon-twitter'] = 2
repo_to_led['craftwork'] = 3


def handler(event, context):

    repo_name = event['body']['repository']['name']
    access_token = event['particle_access_token']
    device_id = event['particle_device_id']

    print 'Received event from repository [' + repo_name + ']'

    data = urllib.urlencode({
        'access_token': access_token,
        'args': repo_to_led.get(repo_name, -1)
    })

    opener = urllib2.build_opener()
    request = urllib2.Request("https://api.particle.io/v1/devices/" + device_id + "/flash", data)

    try:
        connection = opener.open(request)
        data = json.loads(connection.read())

        print 'Success!'
        data['repo_name'] = repo_name

        return data

    except urllib2.HTTPError, e:
        print "Failed to talk to internet button. It's probably not connected: " + str(e)


if __name__ == '__main__':
    handler({
        "particle_access_token": "secret",
        "particle_device_id": "secret",
        "body": {
            "repository": {
                "name": "test-repo"
            }
        }
    }, 0)