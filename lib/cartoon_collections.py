
def roll_call_dwarves(dwarves):
    for index, dwarf in enumerate(dwarves, start=1):
        print(f"{index}. {dwarf}")

def summon_captain_planet(calls):
    return [call.capitalize() + "!" for call in calls]

def long_planeteer_calls(calls):
    return any(len(call) > 4 for call in calls)

def find_the_cheese(items):
    cheese_types = ["cheddar", "gouda", "camembert"]
    for item in items:
        if item in cheese_types:
            return item
    return None

