from typing import Any
from openai import OpenAI
import os
from rich import print
from datasets import load_dataset

dataset = load_dataset("openai/gsm8k", "main", split="train")
dataset = dataset.select(range(2))

def annotate_example(example: dict[str, Any]) -> None:
    api_key = os.environ.get("OPENROUTER_API_KEY")
    client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=api_key)

    response = client.responses.create(
        model="openai/gpt-oss-20b",
        input=[
            {
                "role": "system",
                "content": "Solve the following problem step by step. In your final response to the user, just provide the answer and nothing else.'"
            },
            {
                "role": "user",
                "content": example["question"]
            }
        ],
        reasoning={"effort": "high"},
    )

    reasoning = response.output[0].content[0].text
    response = response.output[1].content[0].text
    example["reasoning"] = reasoning
    example["response"] = response
    return example

dataset = dataset.map(annotate_example, num_proc=16)
dataset.push_to_hub("tomekkorbak/gsm8k-gpt-oss-20b-annotated")