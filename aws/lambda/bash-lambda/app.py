def handler(event, context):
    message = 'Hello bash lambda!'
    return { 
        'message' : message
    }
