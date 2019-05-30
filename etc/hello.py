def application(env, start_response):
    a =  env.QUERY_STRING.replace('&', '\n')
    code = '200 OK'
    headers = [('Content-type', 'text/plain')]
    start_response(code, headers)
    return [ a ]

