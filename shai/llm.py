from langchain_core.callbacks import StdOutCallbackHandler, CallbackManager
from langchain_community.chat_models import ChatLiteLLM


std_out_handler = StdOutCallbackHandler()


# TODO: add more models based on cfg
llm = ChatLiteLLM(
    client=None,
    streaming=True,
    verbose=True,
    max_tokens=4096,
    callback_manager=CallbackManager([std_out_handler]),
    model="gpt-4-0125-preview",
    # model="together_ai/mistralai/Mistral-7B-Instruct-v0.2",
)
