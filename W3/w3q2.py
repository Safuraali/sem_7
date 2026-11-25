family_tree = {
    "Grandfather": ["Father", "Uncle"],
    "Father": ["Son", "Daughter"],
    "Uncle": ["Cousin1", "Cousin2"],
    "Son": ["CHILD1"                                                                          ],
    "Daughter": [],
    "Cousin1": [],
    "Cousin2": []
}


def find_descendants(person, tree):
    descendants = []

    def dfs(current):#rf
        for child in tree.get(current, []):
            descendants.append(child)
            dfs(child)

    dfs(person)
    return descendants


person = "Father"

print("Descendants of", person, ":")
print(find_descendants(person, family_tree))
