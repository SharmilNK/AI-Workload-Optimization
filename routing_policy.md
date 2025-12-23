# Routing Policy (draft)

## Task Type Detection
- classification: short user queries asking to label/categorize a snippet.
- summarization: user asks "summarize" or returns > X tokens of text.
- reasoning: multi-sentence question requiring synthesis.

## Routing Rules (initial)
- classification AND input_tokens < 200 -> small_model (cheapest)
- summarization AND doc_tokens < 1000 -> medium_model
- else -> large_model

## Fallbacks
- If model returns format error -> retry once with adjusted prompt
- If quality_score < 3 -> escalate to large model or human review

## Logging
- Emit event with: request_id, task_type, model_selected, input_tokens, output_tokens, cost_usd_est, quality_score (nullable)
