from openai import OpenAI
import os
from rich import print

api_key = os.environ.get("OPENROUTER_API_KEY")
client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=api_key)

response = client.responses.create(
    model="openai/gpt-oss-20b",
    input="Write a one-sentence bedtime story about a unicorn.",
    reasoning={"effort": "medium"},
)

print(response)

"""
Response(
    id='gen-1761164545-6ojFLQ6K9zM3ICEslG5J',
    created_at=1761164545.0,
    error=None,
    incomplete_details=None,
    instructions=None,
    metadata={},
    model='openai/gpt-oss-20b',
    object='response',
    output=[
        ResponseReasoningItem(
            id='rs_tmp_qh0jx64sxsb',
            summary=[],
            type='reasoning',
            content=[
                Content(
                    text='The user wants: "Write a one-sentence bedtime story about a unicorn." They want a single sentence story appropriate for bedtime. So something like "Under the 
moonlit sky, the gentle unicorn drifted into the colorless meadow where dreams turned into endless silver rainbows." But ensure it\'s one sentence. Let\'s craft something soothing. Let\'s 
produce one sentence. For example: "In the hush of twilight, a silver unicorn dipped its hooves into the crystal pond, and each splash sang a lullaby that carried the stars to the sleepy 
hills." That is one sentence. Or "As the night whispered lullabies, a silvery unicorn trotted through the moonlit fields, leaving glittering footprints that turned softly into dreams for 
every restless child." That\'s also a one-sentence story. Let\'s choose one.\n\nWe must be careful: one sentence, avoid separation by semicolons maybe but still one sentence. Let\'s produce 
a concise, magical, soothing sentence. Can\'t add extra description like "One sentence" or such. Just the story. I\'ll produce: "Beneath the twinkling stars, the gentle unicorn tiptoed 
across the moonlit meadow, leaving a trail of glittering dust that swirled into lullabies for every dreaming child." That is one sentence. Provide as final answer.',
                    type='reasoning_text'
                )
            ],
            encrypted_content=None,
            status=None
        ),
        ResponseOutputMessage(
            id='msg_tmp_clyjtl96v6a',
            content=[
                ResponseOutputText(
                    annotations=[],
                    text='Beneath the twinkling stars, the gentle unicorn tiptoed across the moonlit meadow, leaving a trail of glittering dust that swirled into lullabies for every dreaming
child.',
                    type='output_text',
                    logprobs=None
                )
            ],
            role='assistant',
            status='completed',
            type='message'
        )
    ],
    parallel_tool_calls=True,
    temperature=None,
    tool_choice='auto',
    tools=[],
    top_p=None,
    background=False,
    conversation=None,
    max_output_tokens=None,
    max_tool_calls=None,
    previous_response_id=None,
    prompt=None,
    prompt_cache_key=None,
    reasoning=Reasoning(effort='medium', generate_summary=None, summary=None),
    safety_identifier=None,
    service_tier='auto',
    status=None,
    text=None,
    top_logprobs=None,
    truncation=None,
    usage=ResponseUsage(
        input_tokens=85,
        input_tokens_details=InputTokensDetails(cached_tokens=0),
        output_tokens=310,
        output_tokens_details=OutputTokensDetails(reasoning_tokens=314),
        total_tokens=395,
        cost=4.595e-05,
        is_byok=False,
        cost_details={'upstream_inference_cost': None, 'upstream_inference_input_cost': 2.55e-06, 'upstream_inference_output_cost': 4.34e-05}
    ),
    user=None,
    output_text='',
    store=False
)
"""