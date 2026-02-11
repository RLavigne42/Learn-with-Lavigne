# Thinking With Machines: How LLMs Generate Answers

## Final Output — 1. Introduction: How an AI Decides 'What's Next?'

The easiest mental model is “super-autocomplete.”
AI does not write the whole answer at once.
It predicts the next piece of text, then the next, then the next.
That chain creates a full response.

Your prompt is the starting signal.
It tells the system what topic, tone, and format to aim for.
A vague prompt gives vague output; a clear prompt gives clearer output.

Temperature is a creativity slider:
- lower = safer, more predictable,
- higher = more varied, more creative, but potentially less reliable.

AI also has short-term memory limits.
It cannot hold unlimited text in active focus forever.
If a conversation gets very long, older details can fade or get compressed.

Why repetition loops happen:
if the system falls into a high-probability phrase pattern, it may keep circling similar wording.
This is especially common with weak prompts or overly open-ended instructions.

How to reduce loops:
- ask for structure,
- set constraints,
- request concise output,
- and reset with a clearer prompt when needed.

So answer generation is a controlled prediction stream: prompt in, next-text choices out.
