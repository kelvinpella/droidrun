import asyncio
from droidrun import AgentConfig, DroidAgent, AdbTools, DroidrunConfig, load_llm

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


async def main():
    """
    DroidRun automation
    """
    # Read goal from file
    with open("goal.md", "r") as f:
        goal = f.read().strip()

    models = ["mistralai/devstral-2512:free", "qwen/qwen3-coder:free","nex-agi/deepseek-v3.1-nex-n1:free"]
    tools = AdbTools(serial="emulator-5554")
    llm = load_llm("OpenRouter", models[1])

    # Set maximum execution steps
    # config.agent.max_steps = 999999

    # Create agent with the goal
    agent = DroidAgent(
        goal=goal,
        llms=llm,
        tools=tools,
        config=DroidrunConfig(agent=AgentConfig(max_steps=999999)),
    )

    # Run agent
    result = await agent.run()

    print(f"Success: {result.success}")
    print(f"Reason: {result.reason}")
    if result.get("output"):
        print(f"Output: {result.output}")


if __name__ == "__main__":
    asyncio.run(main())
