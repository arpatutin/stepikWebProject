def application(env, start_response):
    a =  [(i + '\n') for i in env['QUERY_STRING'].split('&')]
    code = '200 OK'
    headers = [('Content-type', 'text/plain')]
    start_response(code, headers)
    return [ a ]

