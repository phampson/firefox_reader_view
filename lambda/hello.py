import json


def handler(event, context):
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/plain'
        },
        'body': 'Fuck you Ridgeline, your path is wrong {}\n'.format(event['path'])
    }
