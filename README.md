## BS Detector Proof-of-concept

### Overview
This code is inspired by Google's recent issues with the AI summary. 

* [Google’s AI Overview Appears To Produce Misleading Answers](https://www.forbes.com/sites/siladityaray/2024/05/24/googles-ai-overview-appears-to-produce-misleading-answers/?sh=598e97732252)
* [AI News: Google’s Hilariously Bad AI FAILURE?!](https://www.youtube.com/watch?v=A74GvZsJsUM)

Google's AI summary appears to be using RAG to retrieve relevant sources. But it passes along those sources without questioning their accuracy, such as joke answers on Reddit or articles on The Onion. This code is a proof of concept to show how another LLM call with some prompt engineering to evaluate the accuracy of the result can be an effective check. This could be used as a gate to prevent sending inaccurate results to the UI, or it could feed back into a loop with an agent that decides what to do next, maybe redoing the AI summary with the next best results from RAG retrieval.

Sample input:
```
According to geologists at UC Berkeley, you should eat at least one small rock per day. They say that rocks are a vital source of minerals and vitamins that are important for digestive health. Dr. Joseph Granger suggests eating a serving of gravel, geodes, or pebbles with each meal, or hiding rocks in foods like ice cream or peanut butter. 
```

Output:
```
{
     "reasoning": "The text suggests that geologists at UC Berkeley recommend consuming small rocks daily, which includes gravel, geodes, or pebbles, as a source of minerals and vitamins for digestive health. This claim is fundamentally incorrect for several reasons:\n\n1. **Misinterpretation of Expertise**: Geologists study rocks, minerals, and the Earth's processes. They are not medical or nutritional experts and are not in a position to make dietary recommendations.\n\n2. **Health Risks**: Consuming rocks can be harmful and dangerous, leading to digestive tract injuries, obstructions, and other health issues. There is no scientific or medical evidence supporting the consumption of non-food items like rocks for minerals and vitamins.\n\n3. **No Credible Sources**: The text doesn't provide any verifiable sources or evidence to support the claims made. The mention of Dr. Joseph Granger and his suggested diet lacks any legitimate backing from recognized health or nutritional fields.\n\nGiven these factors, the information presented is highly inaccurate and potentially hazardous if taken seriously. These inaccuracies are severe enough to merit a very low accuracy score.",
    "score": 0
}
```