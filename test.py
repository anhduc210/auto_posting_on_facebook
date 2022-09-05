import facebook as fb
access_token = "EAALMoZB9vAIsBAL2hLQe6xI8TTi75mImUguW5epRlZAPZApnLIPcObwUXWRQxZCvpSZAUatbdqGCjKSRIdMez1vnwdgEdAZB6Uu12E13QsmTIRZAWwQPNXnBFB4SVxrZAgQX1oTij6LCwFUvBiF0g1t626ewDyCiYZBSSiaaPpU1fZAtfdFWe0oz95"
graph= fb.GraphAPI(access_token)
profile = graph.get_object("me")
print(profile)
x= graph.put_object('me', 'feed', message = 'anhduc')