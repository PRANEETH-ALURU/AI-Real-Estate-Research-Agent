from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool
from pydantic import BaseModel, Field
from typing import List
#from .tools.push_tool import PushNotificationTool
#from crewai.memory import LongTermMemory, ShortTermMemory, EntityMemory
# from crewai.memory.storage.rag_storage import RAGStorage
# from crewai.memory.storage.ltm_sqlite_storage import LTMSQLiteStorage

class LocationResearcher(BaseModel):
    candidate_nhood: str = Field(description="The candidate neighborhoods of the location")
    gen_description: str = Field(description="The general description of the location")
    home_price_range: str =  Field(description="The house price range")
    pop_growth_indicators:str  = Field(description="The population growth indicators")
    major_employers_near: str = Field(description="The major employers nearby")

class LocationResearcher_List(BaseModel):
    loc_res_list: List[LocationResearcher] = Field(description="List of candidate neighborhoods")
    

class NeighborhoodMarketDataAnalyst(BaseModel):
    neighborhood_name: str = Field(description="Name of the neighborhood")
    median_home_price: str = Field(description="Current median home price")
    one_year_appreciation: str = Field(description="Home price appreciation over the last 1 year")
    inventory_trends: str = Field(description="Current housing inventory trend in the neighborhood")
    days_on_market: str = Field(description="Average number of days homes stay on the market")
    buyer_demand: str = Field(description="Current buyer demand level in the neighborhood")


class NeighborhoodMarketDataList(BaseModel):
    neighborhoods: List[NeighborhoodMarketDataAnalyst] = Field(
        description="List of neighborhood-level real estate market data"
    )

class NeighborhoodEvaluator(BaseModel):
    name: str = Field(description="The name of the neighborhood")
    Pros: List[str] =  Field(description="The advantages of living in the neighborhood")
    Cons: List[str] = Field(description="The disadvantes of living in the neighborhood")
    overall_assessment: str = Field(description="The overall assessment of the neighborhood to check suitable or not")
    
class NeighborhoodEvaluatorList(BaseModel):
    neighborhood: List[NeighborhoodEvaluator] = Field(description="The list of neighborhood pros, cons and summary")
    

@CrewBase
class RealEstate():
    
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'
    
    @agent
    def Location_Researcher(self) -> Agent:
        return Agent(config = self.agents_config['Location_Researcher'], tools = [SerperDevTool()], memory = True)
    
    @agent
    def Neighborhood_Market_Data_Analyst(self) -> Agent:
        return Agent(config = self.agents_config['Neighborhood_Market_Data_Analyst'], tools = [SerperDevTool()], memory = True)
    
    @agent
    def neighborhood_evaluator(self) -> Agent:
        return Agent(
            config=self.agents_config["Neighborhood_Evaluator"],
            tools=[SerperDevTool()],
            memory=True,
        )
    @agent
    def real_estate_advisor(self) -> Agent:
        return Agent(
            config=self.agents_config["Real_Estate_Advisor"],
            tools=[SerperDevTool()],
            memory=True,
        )
    @agent
    def manager(self) -> Agent:
        return Agent(
            config=self.agents_config["Manager"],
            allow_delegation=True,
            memory=True,
        )
    
    @task
    def find_location(self) -> Task:
        return Task(config = self.tasks_config['find_location'], output_pydantic = LocationResearcher_List)
    
    @task
    def neighborhood_analysis(self) -> Task:
        return Task(
            config=self.tasks_config["neighborhood_analysis"],
            output_pydantic=NeighborhoodMarketDataList,
        )

    @task
    def neighborhood_evaluator_task(self) -> Task:
        return Task(
            config=self.tasks_config["neighborhood_evaluator_task"],
            output_pydantic=NeighborhoodEvaluatorList,
        )


    @task
    def final_recommendation(self) -> Task:
        return Task(
            config=self.tasks_config["final_recommendation"],
        )
        
    
    @crew
    def crew(self) -> Crew:
        
        manager = Agent(
            config=self.agents_config["Manager"],
            allow_delegation=True,
            memory=True,
        )

        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.hierarchical,
            verbose=True,
            manager_agent=manager,
            memory=True,
        )
