def find_ancestors(ancestors, starting_node):
    # create an empty list ancestors
    ancestors = []
    # loop through the input list of tuples
    for parent, child in ancestors:
        # see if the child is starting_node
        if child == starting_node:
            # add the parent to ancestors
            ancestors.append(parent)

    # if ancestors is empty return -1
    if not len(ancestors):
        return -1
    # otherwise, return ancestors
    else:
        return ancestors


def earliest_ancestor(ancestors, starting_node):
    pass
