import os
import json
import boto3
import urllib.parse
import urllib.request

from app import get_completion

SLACK_BOT_TOKEN = os.environ['BOT_TOKEN']


def post_message_to_channel(channel_id, prompt):
    # Construct the Slack API URL
    url = "https://slack.com/api/chat.postMessage"
    message = get_completion(prompt)
    # Set the API headers
    headers = {
        "Content-type": "application/json",
        "Authorization": "Bearer " + SLACK_BOT_TOKEN
    }
    # Set the API payload
    payload = {
        "channel": channel_id,
        "text": message
    }
    # Send the API request
    req = urllib.request.Request(url, data=json.dumps(payload).encode('utf-8'), headers=headers, method='POST')
    response = urllib.request.urlopen(req)


def lambda_handler(event, context):
    # Verify that the request came from Slack
    if 'challenge' in event:
        return {'challenge': event['challenge']}
    else:
        # Parse the Slack event
        slack_body = event.get("body")
        slack_body_json = json.loads(slack_body)
        slack_event = slack_body_json.get("event")
        print('Event: ', event)
        channel_id = slack_event.get("channel")

        element_text = slack_event.get("text")
        bot_id = slack_event.get('bot_id')
        if bot_id:
            print("message comes from bot, EXITING")
            return {'statusCode': 200}
        # Post a message to the channel
        post_message_to_channel(channel_id, element_text)
        return {'statusCode': 200}
