import asyncio
import os
from pyrit.prompt_target import OpenAIChatTarget
from pyrit.setup import initialize_pyrit_async, IN_MEMORY
from pyrit. models.messages import Message, MessagePiece

# Route PyRIT to Ollama and set all required environment variables
os.environ["OPENAI_CHAT_ENDPOINT"] ="http://localhost:11434/v1"
os.environ["OPENAI_CHAT_KEY"] = "ollama-local"
os.environ["OPENAI_CHAT_MODEL"] = "llama3.2:1b"

async def main():
    # Asynchronously initialize PyRIT's central memory database
    await initialize_pyrit_async(memory_db_type=IN_MEMORY)

    target = OpenAIChatTarget(model_name="llama3.2:1b")

    # Use 'original_value' instead of 'content' to satisfy Pydantic
    piece = MessagePiece(role="user", original_value="Hello! Are you receiving my prompt via PyRIT?")
    msg = Message(message_pieces=[piece])

    # Send the correctly formatted Message object
    response = await target.send_prompt_async(message=msg)

    print(f"Connection Successful. Model Output:\n{response[0].message_pieces[0].original_value}")

if __name__ == "__main__":
    asyncio.run(main())
