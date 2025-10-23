"""
GSM8K evaluation.
https://huggingface.co/datasets/openai/gsm8k

Example problem instance:

Question:
Weng earns $12 an hour for babysitting. Yesterday, she just did 50 minutes of babysitting. How much did she earn?
Answer:
Weng earns 12/60 = $<<12/60=0.2>>0.2 per minute.
Working 50 minutes, she earned 0.2 x 50 = $<<0.2*50=10>>10.
#### 10

Notice that GSM8K uses tool calls inside << >> tags.
"""

from datasets import load_dataset
from tasks.gsm8k import GSM8K


class GSM8KQStarTeacher(GSM8K):

    def __init__(self, subset, split, **kwargs):
        super().__init__(subset, split,**kwargs)
        assert subset in ["main"], "GSM8K subset must be main|socratic"
        assert split in ["train"], "GSM8K split must be train|test"
        self.ds = load_dataset("tomkita/gsm8k-gpt-oss-20b-annotated", split=split).shuffle(seed=42)

    def get_example(self, index):
        """ Get a single problem from the dataset. """
        row = self.ds[index]
        question = row['question'] # string of the question prompt
        reasoning = row['teacher_reasoning'] # string of the full solution and the answer after #### marker
        answer = row['teacher_answer'] # string of the full solution and the answer after #### marker
        # Create and return the Conversation object
        assistant_message_parts = [
            {"type": "reasoning", "text": reasoning},
            {"type": "text", "text": answer},
        ]
        # No put it all together
        messages = [
            {"role": "user", "content": question}, # note: simple string
            {"role": "assistant", "content": assistant_message_parts}, # note: list of parts (as dicts)
        ]
        conversation = {
            "messages": messages,
        }
        return conversation
