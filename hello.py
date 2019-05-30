def application(env, start_response):
    a =  [bytes(i + '\n', 'ascii') for i in environ['QUERY_STRING'].split('&')]
    code = '200 OK'
    headers = [('Content-type', 'text/plain')]
    start_response(code, headers)
    return [ a ]

