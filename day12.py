connections = """pg-CH
pg-yd
yd-start
fe-hv
bi-CH
CH-yd
end-bi
fe-RY
ng-CH
fe-CH
ng-pg
hv-FL
FL-fe
hv-pg
bi-hv
CH-end
hv-ng
yd-ng
pg-fe
start-ng
end-FL
fe-bi
FL-ks
pg-start"""

# From connections A-C, B-C, we create a graph { "A": ["C"], "B": ["C"], "C": ["A", "B"] }
graph = {}

for connection in connections.splitlines():
    def connect(from_, to):
        if not (destinations := graph.get(from_)):
            destinations = []
            graph[from_] = destinations
        destinations.append(to)

    start, end = connection.split("-")
    connect(start, end)
    connect(end, start)

# Sort the connections alphabetically so the order of the output matches that in the examples given (Only for debugging & troubleshooting) 
for from_, to in graph.items():
    to.sort()

# Recursively walk from start to the next possible paths, stopping at end or paths with no possible next moves

def is_any_visited_twice(walked):
    # Part 1
    #return False
    # Part 2
    from collections import Counter
    counts = Counter(filter(lambda item: item.islower(), walked))
    return any(filter(lambda item: item > 1, counts.values()))

def walk(cur_loc, walked):
    valid_next = []
    visited_twice = is_any_visited_twice(walked)
    for potential_next in graph[cur_loc]:
        if potential_next == "start":
            continue
        if visited_twice and potential_next.islower() and potential_next in walked:
            continue
        valid_next.append(potential_next)
    
    if len(valid_next) == 0:
        return
    
    forks = []
    for next in valid_next:
        fork = walked.copy()
        fork.append(next)
        if next == "end":
            forks.append(fork)
            continue
        if result := walk(next, fork):
            forks += result
    return forks

paths = walk("start", ["start"])

for path in paths:
    print("-".join(path))

print("number of paths = ", len(paths))