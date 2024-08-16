import os
import litellm

# Set Environment Variables
if os.environ.get("OPENAI_API_KEY") is None:
    os.environ["OPENAI_API_KEY"] = ""
if os.environ.get("OPENAI_BASE_URL") is None:
    os.environ["OPENAI_BASE_URL"] = ""

os.environ["LANGSMITH_API_KEY"]
os.environ["LANGSMITH_PROJECT"] = "litellm_colab" 
os.environ["LANGSMITH_DEFAULT_RUN_NAME"] = "" # defaults to LLMRun


litellm.set_verbose = True

from agents.task.solution import Solution, SolutionConfig


query = "task: Design a system of LLM agents to create a comprehensive 'site comprehension API' that: " \
        "objectives: Analyzes a given website's structure, content, and navigation patterns. " \
        "Develops a deep understanding of the site's architecture and data organization. " \
        "Generates optimized scraping code based on this understanding, without redundant exploration. " \
        "Creates an API that can answer queries about the site's content and structure. " \
        "system_requirements: Utilize a team of specialized LLM agents, each focusing on different aspects (e.g., site structure analysis, content categorization, code generation). " \
        "Implement efficient token usage strategies to minimize redundant processing. " \
        "Produce scraping code that is accurate, efficient, and adaptable to site updates. " \
        "Provide an interface for users to query site information without needing to re-scrape or re-analyze. " \
        "api_capabilities: Answering complex queries about the site's content and structure. " \
        "Generating targeted scraping code for specific data extraction tasks. " \
        "Performing all functions without requiring additional site exploration."

solution_config = SolutionConfig.generate_config(query)
# Save the config to a file
solution_config.save("playground/configs/SOP.json")
solution = Solution(config=solution_config)
solution.dump("./openai_tests/config")
#solution.run()