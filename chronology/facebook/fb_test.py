import facebook
from pprint import pprint

graph = facebook.GraphAPI(access_token="338938349924993|BlDmbQBsIcfZzse96Y19v6JcNx0", version="2.11")

# Get the message from a post.
post = graph.get_object(id='thepsybus', fields='events')
pprint(post['events']['paging'])
pprint(post['events']['data'])
