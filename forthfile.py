import validators
validators.url("http://google.com")
True
validators.url("http://google")
ValidationFailure(func=url, args={'value': 'http://google', 'require_tld': True})
if not validators.url("http://google"):
 print ("not valid")