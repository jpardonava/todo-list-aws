import json
import decimalencoder
import todoList


def translate(event, context):
    # create a response
    id_dato = event['pathParameters']['id']
    lang = event['pathParameters']['lang']
    item = todoList.get_item_trans(id_dato, lang)
    if item:
        response = {
            "statusCode": 200,
            "body": json.dumps(item,
                               cls=decimalencoder.DecimalEncoder)
        }
    else:
        response = {
            "statusCode": 404,
            "body": ""
        }
    return response
