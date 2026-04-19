from duckduckgo_search import DDGS


def search_destination(destination):
    places = []

    try:
        with DDGS() as ddgs:
            results = ddgs.text(
                f"top tourist attractions in {destination}",
                max_results=5
            )

            for r in results:
                places.append(r["title"])

    except:
        places = ["City Museum", "Local Market"]

    return places


def estimate_budget(days, budget_type):

    days = int(days)

    if budget_type == "low":
        total = days * 2500
    elif budget_type == "medium":
        total = days * 5000
    else:
        total = days * 9000

    return f"Estimated total budget for {days} days: ₹{total}"


def travel_tips():

    return [
        "Carry sunscreen and a water bottle",
        "Check weather forecast before traveling",
        "Keep digital copies of documents",
        "Try authentic local food safely"
    ]