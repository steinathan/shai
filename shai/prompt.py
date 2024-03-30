import os
import platform

from langchain.prompts import PromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain.output_parsers import PydanticOutputParser


class CmdOutput(BaseModel):
    command: str = Field(description="the generated linux command to run")


tmpl = """
You are an expert at using shell commands, and someone has asked you to translate their instructions into Linux commands which according to the text below

[(System Info)]: {system_info}

[(Instruction)]: {question}

{format_instructions}
Never give explanations or whatsoever only the formated JSON!!!
"""

output_parser = PydanticOutputParser(pydantic_object=CmdOutput)

system_info = {
    "Home Directory": os.path.expanduser("~"),
    "System": platform.system(),
    "Machine": platform.machine(),
    "Processor": platform.processor(),
}

prompt = PromptTemplate(
    template=tmpl,
    input_variables=["question"],
    partial_variables={
        "format_instructions": output_parser.get_format_instructions(),
        "system_info": system_info,
    },
)
