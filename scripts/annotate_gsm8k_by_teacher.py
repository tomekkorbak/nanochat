from typing import Any

import sys

sys.path.append(".")
from tasks.gsm8k import extract_answer
from openai import OpenAI
import os
from rich import print
from datasets import load_dataset

DATASET_SIZE = 2_000
FORBIDDEN_SUBSTRINGS = ["<think>"]

dataset = load_dataset("openai/gsm8k", "main", split="train")
dataset = dataset.select(range(DATASET_SIZE))

def annotate_example(example: dict[str, Any]) -> None:
    reasoning = None
    final_answer = None
    while not reasoning or not final_answer:
        try:
            api_key = os.environ.get("OPENROUTER_API_KEY")
            client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=api_key)

            response = client.responses.create(
                model="openai/gpt-oss-20b",
                input=[
                    {
                        "role": "system",
                        "content": "Solve the following problem step by step. Then format your final answer as '#### <answer>'"
                    },
                    {
                        "role": "user",
                        "content": example["question"]
                    }
                ],
                reasoning={"effort": "medium"},
            )

            if len(response.output) != 2:
                print(f"Error: response output length is not 2; retrying")
                continue

            reasoning = response.output[0].content[0].text
            full_answer = response.output[1].content[0].text

            if any(substr in full_answer for substr in FORBIDDEN_SUBSTRINGS):
                print(f"Error: forbidden substring found in full_answer; retrying")
                continue

            if extract_answer(full_answer) is None:
                print(f"Error: extracted answer is None")
                continue

            final_answer = full_answer
        except Exception as e:
            print(f"Error: {e}")
            continue

    example["original_answer"] = example["answer"]
    del example["answer"]
    example["teacher_reasoning"] = reasoning
    example["teacher_answer"] = final_answer
    return example

dataset = dataset.map(annotate_example, num_proc=16)
dataset.push_to_hub("tomkita/gsm8k-gpt-oss-20b-annotated")