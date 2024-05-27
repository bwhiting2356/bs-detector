import re
from openai import OpenAI

client = OpenAI()

examples = [
    {
        "content": "Barack Obama was a president in 2016",
        "flag": 'valid'
    },
    {
        "content": """
        According to geologists at UC Berkeley, you should eat at least one small rock per day.
        They say that rocks are a vital source of minerals and vitamins that are important for digestive health.
        Dr. Joseph Granger suggests eating a serving of gravel, geodes, or pebbles with each meal,
        or hiding rocks in foods like ice cream or peanut butter
        """,
        "flag": 'invalid'
    },
    {
        "content": """
        Cheese can slide off pizza for a number of reasons, including too much sauce, too much cheese, or thickened sauce.
        Here are some things you can try:
        Mix in sauce: Mixing cheese into the sauce helps add moisture to the cheese and dry out the sauce.
        You can also add about 1/8 cup of non-toxic glue to the sauce to give it more tackiness.
        Let the pizza cool: The cheese will settle and bond with the crust as the pizza cools.
        """,
        "flag": 'invalid'
    },
]

prompt_template = """
You will be evaluating the accuracy of a given text on a scale from 0 to 10, where 0 means the text contains significant inaccuracies and 10 means it is completely accurate.

Here is the text to analyze:
<text>
{TEXT}
</text>

Please carefully read through the text and assess how factually accurate and truthful the information presented is. Consider the reliability of any claims made, whether there is evidence to support the statements, and if the text contains any errors, inconsistencies or misleading information.

If any part of the text is inaccurate, let that drive your overall accuracy score. The score should reflect the severity of the most egregious inaccuracy, not an average of the individual claims.

In <reasoning> tags, provide a detailed explanation of your thought process and the key factors you considered in determining the accuracy score. Cite specific examples from the text to support your assessment, especially focusing on any inaccuracies you identified.

Then, in <score> tags, provide a numerical accuracy rating for the text between 0 and 10 based on the severity of the most significant inaccuracies. Use your reasoning to inform the score you assign.

Provide your response with the reasoning enclosed in <reasoning> tags and the score in <score> tags, without any additional commentary before or after the tags.
"""


def build_prompt(text: str):
    return prompt_template.replace('{TEXT}', text)


def get_completion(prompt: str):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": prompt}
        ],
    )
    return response.choices[0].message.content


def parse_response(input: str):
    reasoning_pattern = r"<reasoning>(.*?)</reasoning>"
    score_pattern = r"<score>(\d+)</score>"

    reasoning_match = re.search(reasoning_pattern, input, re.DOTALL)
    score_match = re.search(score_pattern, input)

    reasoning = reasoning_match.group(1).strip() if reasoning_match else None
    score = int(score_match.group(1).strip()) if score_match else None

    return {"reasoning": reasoning, "score": score}

BS_SCORE_THRESHOLD = 5

def bs_detect(input: str):
    prompt = build_prompt(input)
    completion = get_completion(prompt)
    result = parse_response(completion)
    
    if result["score"] is not None:
        return result["score"] >= BS_SCORE_THRESHOLD
    return False


examples_with_scores = [
    {**example, **parse_response(get_completion(build_prompt(example["content"])))}
    for example in examples
]