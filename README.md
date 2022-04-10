# Heroku-Flask-Limiter-Test
Just a test to checkout Flask Limiter on Heroku.  

Wanted to check if it's true that Heroku changes the IP address of the remote client.  
Turned out it's true and it breaks the usage of Flask-Limiter as it relies on storing the IPs to rate limit the routes.  

The solution was to use a ProxyFix from the werkzeug helper module.  
This replaces the contents of the remote_client header to the contents of the X-Forwarded-For header.  

This ensures that the IPs are the same and rate limiting works as expected.  

I haven't checked whether or not it can be bypassed using some special request with a different X-Forwarded-For header.  
