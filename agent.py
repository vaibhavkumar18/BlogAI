# from google.adk.agents import LlmAgent

# # dummy root – required for ADK to initialize
# root_agent = LlmAgent(
#     model="gemini-2.5-flash",
#     name="root_agent",
#     description="Router agent that forwards work to backend pipelines.",
#     instruction="""
# You are a router agent. 
# Do NOT generate content.
# Reply with: 'OK'.
# """
# )


from .blog_agent import blog_pipeline
root_agent=blog_pipeline