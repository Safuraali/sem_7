site = {
    'Home': {
        'About': {},
        'Products': {
            'Electronics': {},
            'Books': {}
        },
        'Contact': {}
    }
}
def find_page(tree, target, path=None):
    if path is None:
        path = []
    for page, children in tree.items():
        current_path = path + [page]
        if page == target:
            return current_path
        result = find_page(children, target, current_path)
        if result:
            return result
    return None
target = "Books"
path = find_page(site, target)
if path:
    print("Path:", " -> ".join(path))
else:
    print("Page not found.")


