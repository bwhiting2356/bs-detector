### BS Detector Proof-of-concept

## Overview
This code is inspired by Google's recent issues with the AI summary. 
Links:
* [Google’s AI Overview Appears To Produce Misleading Answers](https://www.forbes.com/sites/siladityaray/2024/05/24/googles-ai-overview-appears-to-produce-misleading-answers/?sh=598e97732252)
* [AI News: Google’s Hilariously Bad AI FAILURE?!](https://www.youtube.com/watch?v=A74GvZsJsUM)

Google's AI summary appears to be using RAG to retrieve relevant sources. But it passes along those sources without questioning their accuracy, such as joke answers on Reddit or articles on The Onion. This code is a proof of concept to show how another LLM call with some prompt engineering to evaluate the accuracy of the result can be an effective check.