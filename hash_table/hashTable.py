# Hash table

# The server works only if the URL is not stored in the cache.
# However, before you return the data, you save it to the cashe.
# When the user next requests the same URL, the data can be sent to the cache 
# (instread of forcing the server to fo the work)
#                                                            page 100 chapter 5
# -----------------------------------------------------------------------------

def get_data_for_server(url):
    return url


cache = {}
def get_url(url):
    if cache.get(url) != None:
        return cache[url]               # return cache data
    else:                               # the server works only if the URL is not stored in the cashe
        data = get_data_for_server(url)
        cache[url] = data               # data is first stored in the cache
        return data                 
        