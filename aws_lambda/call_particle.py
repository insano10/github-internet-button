import json
import urllib
import urllib2


# bit hacky but lump pull_request and comment together as conversation comments on pull requests get notified
# under the issue comment webhook
def get_event_type(request_body):
    if request_body.get('pusher') is not None:
        return 'Push'
    elif request_body.get('pull_request') or request_body.get('comment') is not None:
        return 'PullRequest'
    else:
        return 'Unknown'


def handler(event, context):

    repo_name = event['body']['repository']['name']
    access_token = event['particle_access_token']
    device_id = event['particle_device_id']
    event_type = get_event_type(event['body'])


    # ignore pushes to branches other than master
    if event_type == 'Push' and event['body']['ref'] != 'refs/heads/master':
        exit()

    print 'Received ' + event_type + ' event from repository [' + repo_name + ']'

    data = urllib.urlencode({
        'access_token': access_token,
        'args': event_type
    })

    opener = urllib2.build_opener()
    request = urllib2.Request("https://api.particle.io/v1/devices/" + device_id + "/notify", data)

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
            },
            "pusher": "someone@somewhere.com"
        }
    }, 0)