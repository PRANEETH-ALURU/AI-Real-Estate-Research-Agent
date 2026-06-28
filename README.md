# AI Real Estate Research Agent

This project is a multi-agent AI application built using CrewAI that helps users identify promising neighborhoods for purchasing a home or investment property.

Given a location, budget, and buyer goal, the system performs live web research, analyzes real estate market trends, evaluates neighborhoods, and recommends the best options based on affordability, growth potential, and investment value.

## Features

- Multi-agent workflow using CrewAI
- Live web search with Serper API
- Streamlit web interface
- Neighborhood market analysis
- Investment scoring and ranking
- Budget-aware recommendations
- Downloadable recommendation report

## Tech Stack

- Python
- CrewAI
- OpenAI GPT-4o Mini
- Serper API
- Streamlit
- Pydantic

## Screenshots

### Home Page

![Home Page](assets/home_page.png)

### Candidate Neighborhoods

![Candidate Neighborhoods](assets/candidate_neighbors.png)

### Neighborhood Analysis

![Neighborhood Analysis](assets/neighbor_description.png)

### Final Recommendation

![Final Recommendation](assets/risks_nextsteps_downloadreport.png)

## Installation

Clone the repository

```bash
git clone git@github.com:PRANEETH-ALURU/AI-Real-Estate-Research-Agent.git
```

Move into the project

```bash
cd AI-Real-Estate-Research-Agent
```

Install dependencies

```bash
uv sync
```

Create a `.env` file in the project root.

```text
OPENAI_API_KEY=your_openai_api_key
SERPER_API_KEY=your_serper_api_key
```

## Run the Application

Launch the Streamlit application:

```bash
uv run streamlit run src/real_estate_ai_agent/app.py
```

Then open the URL displayed in the terminal (usually http://localhost:8501).

## Project Structure

```
AI-Real-Estate-Research-Agent/
│
├── assets/
├── config/
├── src/
├── output/
├── pyproject.toml
└── README.md
```

## Future Improvements

- Interactive map visualization
- Rental yield estimation
- Crime and school rating analysis
- Property listing integration
- PDF report generation

## Author

Praneeth Aluru