#!/usr/bin/env python
from datetime import datetime
from real_estate_ai_agent.crew import RealEstate


def run():
    """Run the real estate research crew."""

    inputs = {
        "location": "Charlotte, NC",
        "budget": "$450,000",
        "buyer_goal": "investment property",
        "current_date": str(datetime.now()),
    }

    result = RealEstate().crew().kickoff(inputs=inputs)

    print("\n\n=== FINAL REAL ESTATE RECOMMENDATION ===\n")
    print(result.raw)


if __name__ == "__main__":
    run()