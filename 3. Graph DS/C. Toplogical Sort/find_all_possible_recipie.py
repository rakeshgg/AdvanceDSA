from collections import defaultdict
from queue import Queue
'''
We have a list of n recipes. We also have the ingredients
of each of these recipes in a 2D array ingredients where
ingredients[i] is the array of ingredients of recipes[i].
And we have a list supplies that represents ingredients
we initially have, in infinite quantity. The goal is to
find out what possible recipes we can prepare and return
that list in any order. Note that recipes can be ingredients to each other.

input:

recipes = ["chicken burger", "buns", "crispy chicken"]
ingredients = [["buns", "crispy chicken", "lettuce", "cheese"], ["yeast", "flour"], ["chicken", "breadcrumbs"]]
supplies = ["yeast", "flour", "cheese", "breadcrumbs", "milk", "lettuce", "chicken"]

output: ["buns", "crispy chicken", "chicken burger"]

explanation: We start by preparing buns, then we prepare crispy
chicken, then we can prepare chicken burger.

https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/

|ingredients| = |recipes| = n
n ≥ 1
|ingredients[i]| ≥ 1
|supplies| ≥ 1

'''

'''
prepered = []
for recipe in recipse:
  if ingredients[recipe] subset of supplies:
    prepered.add(recipe)
return prepered

'''


def toplogical_sort(graph):
    # count in degree
    # creating default 0 for indegree
    # adjancy list
    # visted set not required used when adding same vertex multiple time
    # each vertex is added to queue exactly once if indegree is 0
    indegree = defaultdict(lambda: 0)
    for u in graph:
        for v in graph[u]:
            indegree[v] += 1
    queue = Queue()
    # adding indegree 0 in queue
    for vertex in graph:
        if indegree[vertex] == 0:
            queue.put(vertex)
    ordering = []
    while not queue.empty():
        vertex = queue.get()
        ordering.append(vertex)
        for neighbor in graph[vertex]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.put(neighbor)
    # if cycle inderdepency - nothing queue
    if len(ordering) < len(graph):
        # returen recipies which can be prepared even if ordering is not complete
        return ordering
    return ordering


def find_recipes(recipes, ingredients, supplies):
    # lets covert the input in graph adjnacy list
    ingredients = {recipes[i]: set(ingredients[i]) for i in range(len(ingredients))}
    supplies = set(supplies)
    graph = {recipe: [] for recipe in recipes}
    for u in recipes:
        for v in recipes:
            if u in ingredients[v]:
                graph[u].append(v)
    ordering = toplogical_sort(graph)
    # how to handle this - recipe in cycle cant be prepared
    prepared = []
    for recipe in ordering:
        if ingredients[recipe].issubset(supplies):
            prepared.append(recipe)
            # used in next recipie
            supplies.add(recipe)
    return prepared

# TC: n^2


if __name__ == '__main__':
    recipes = ["chicken burger", "buns", "crispy chicken"]
    ingredients = [["buns", "crispy chicken", "lettuce", "cheese"], ["yeast", "flour"], ["chicken", "breadcrumbs"]]
    supplies = ["yeast", "flour", "cheese", "breadcrumbs", "milk", "lettuce", "chicken"]

    print('Possible recipes are:', find_recipes(recipes, ingredients, supplies))
    # Output: Possible recipes are: ['buns', 'crispy chicken', 'chicken burger']
