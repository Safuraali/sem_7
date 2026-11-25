log1_events = ["A101", "B202", "C303", "A101", "D404"]
log2_events = {"C303", "E505", "F606", "B202"}

log1_events = set(log1_events)

common_events = log1_events.intersection(log2_events)

all_events = log1_events.union(log2_events)

print("Unique events in Log 1:", log1_events)
print("Common events:", common_events)
print("All unique events:", all_events)
