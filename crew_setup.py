from crewai import Crew, Task
from agent_definitions import (
    research_agent,
    planner_agent,
    budget_agent,
    writer_agent,
    review_agent
)

research_task = Task(
    description="""
Find the top tourist attractions and famous foods in {destination}.
Return a short list of important places.
""",
    agent=research_agent,
    expected_output="List of attractions"
)

planning_task = Task(
    description="""
Create a travel itinerary for {destination}.

IMPORTANT:
You MUST create exactly {days} days.

Format strictly like this:

Day 1:
- activity
- activity

Day 2:
- activity
- activity

Continue until Day {days}.
""",
    agent=planner_agent,
    expected_output="Day-wise itinerary"
)

budget_task = Task(
    description="""
Estimate total travel cost for {days} days in {destination}
with a {budget} budget.
""",
    agent=budget_agent,
    expected_output="Estimated travel cost"
)

writing_task = Task(
    description="""
Combine research, itinerary and budget into a final travel plan.

The itinerary MUST keep the same structure:

Day 1
Day 2
Day 3
until Day {days}.
""",
    agent=writer_agent,
    expected_output="Structured itinerary"
)

review_task = Task(
    description="Improve readability of the itinerary.",
    agent=review_agent,
    expected_output="Final improved itinerary"
)

crew = Crew(
    agents=[
        research_agent,
        planner_agent,
        budget_agent,
        writer_agent,
        review_agent
    ],
    tasks=[
        research_task,
        planning_task,
        budget_task,
        writing_task,
        review_task
    ],
    verbose=True
)