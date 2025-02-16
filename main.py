from smolagents import CodeAgent, HfApiModel

import  os

model_id = "meta-llama/Llama-3.3-70B-Instruct"
hf_token = os.getenv("HF_API_KEY")

model = HfApiModel(token=hf_token) #

agent = CodeAgent(tools=[], model=model, add_base_tools=True)
agent.run(
    "Give me square root of 100",
)