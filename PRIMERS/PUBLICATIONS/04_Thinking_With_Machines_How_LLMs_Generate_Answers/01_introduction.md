# Booklet Title
Thinking With Machines: How LLMs Generate Answers

## Section Title
1. Introduction: How an AI Decides 'What's Next?'

## url_slug
`primer/generation-how-llms-think`

## Short Question
How does an AI generate each next word, and why do settings and memory limits affect the output?

## Long-Form Guidance Question
Provide an intuitive, conceptual guide to the 'inference' (generation) process. You *must not* use terms like 'inference', 'autoregressive', or 'KV cache'. (1) Explain the core idea as 'super-autocomplete' (e.g., 'The AI is *always* just predicting the 'most likely' next word or 'Lego block' based on all the words that came before it'). (2) Explain 'prompts' as the 'starting-point' (e.g., 'giving the AI the first half of a sentence and asking it to finish'). (3) Explain 'temperature' using a simple metaphor like 'a creativity slider' (e.g., 'Temperature 0 = the most boring, predictable, "safe" next word. Temperature 1 = a more creative, wild, "risky" next word'). (4) Explain 'context limits' *without* using the word 'window' (e.g., 'An AI has a 'short-term memory' and can only 'remember' the last 10 pages of your chat; it forgets everything that came before.'). (5) Explain 'stuck loops' (e.g., 'why the AI sometimes gets 'stuck' and repeats the same phrase over and over').

## JSON Representation
```json
{
  "booklet_title": "Thinking With Machines: How LLMs Generate Answers",
  "section_title": "1. Introduction: How an AI Decides 'What's Next?'",
  "url_slug": "primer/generation-how-llms-think",
  "short_question": "How does an AI generate each next word, and why do settings and memory limits affect the output?",
  "long_form_question": "Provide an intuitive, conceptual guide to the 'inference' (generation) process. You *must not* use terms like 'inference', 'autoregressive', or 'KV cache'. (1) Explain the core idea as 'super-autocomplete' (e.g., 'The AI is *always* just predicting the 'most likely' next word or 'Lego block' based on all the words that came before it'). (2) Explain 'prompts' as the 'starting-point' (e.g., 'giving the AI the first half of a sentence and asking it to finish'). (3) Explain 'temperature' using a simple metaphor like 'a creativity slider' (e.g., 'Temperature 0 = the most boring, predictable, \"safe\" next word. Temperature 1 = a more creative, wild, \"risky\" next word'). (4) Explain 'context limits' *without* using the word 'window' (e.g., 'An AI has a 'short-term memory' and can only 'remember' the last 10 pages of your chat; it forgets everything that came before.'). (5) Explain 'stuck loops' (e.g., 'why the AI sometimes gets 'stuck' and repeats the same phrase over and over')."
}
```
