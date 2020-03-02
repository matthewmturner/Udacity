# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self):
        # Initialize the node with children as before, plus a handler
        self.is_valid_url = False
        self.children = {}
        self.handler = None


# The Router class will wrap the Trie and handle
class Router:
    def __init__(self, root_handler, not_found_handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.root = RouteTrieNode()
        self.root_handler = root_handler
        self.not_found_handler = not_found_handler

    def add_handler(self, url, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        if url[0] != "/":
            raise ValueError("Url must start at root '/'")
        url_parts = self._split_path(url)
        current = self.root
        for part in url_parts:
            if part not in current.children.keys():
                current.children[part] = RouteTrieNode()
                current.children[part].handler = self.not_found_handler
            current = current.children[part]

        current.is_valid_url = True
        current.handler = handler

    def lookup(self, url):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        if (url == "/") or (url == ""):
            return self.root_handler
        url_parts = self._split_path(url)
        current = self.root
        for part in url_parts:
            if part not in current.children:
                return self.not_found_handler
            current = current.children[part]

        return current.handler

    def _split_path(self, url):
        # you need to split the path into parts for
        # both the add_handler and lookup functions,
        # so it should be placed in a function here
        url_parts = url.split("/")
        if url_parts[-1] == "":
            url_parts.pop()

        return url_parts


# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router(
    "root handler", "not found handler"
)  # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

print(router.lookup("/"))
# Expected output: 'root handler'
print(router.lookup(""))
# Expected output: 'root handler'
print(router.lookup("/home"))
# Expected output: 'not found handler'
print(router.lookup("/home/about"))
# Expected output: 'about handler'
print(router.lookup("/home/about/"))
# Expected output: 'about handler'
print(router.lookup("/home/about/me"))  # Expected output: 'not found handler'
router.add_handler("home/here", "home here handler")
# Expected output: ValueError Url must start at root '/'
