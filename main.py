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

    tools = AdbTools(serial="emulator-5554")
    llm = load_llm("OpenRouter", "mistralai/devstral-2512:free")

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
