# Sources

- https://github.com/mahimairaja/awesome-voice-apps/tree/7ee5154b5b83943dc0e9fa3f587d3bdf221a4338/demos/panel-scribe : agent code quoted in the post (on_user_turn_completed with StopResponse, the stt_node tee, PyannoteLive sidecar, publish_scorecard, INSTRUCTIONS).
- https://github.com/mahimairaja/awesome-voice-apps/blob/7ee5154b5b83943dc0e9fa3f587d3bdf221a4338/tests/panel-scribe/test_sidecar.py : the offline sidecar tests.
- https://github.com/mahimairaja/awesome-voice-apps/pull/75 : the hosted adapter (hosted_panel.py): spoken handoff regex, SpokenPanel, typed ScorecardRow.
- livekit-agents 1.8.5, livekit/plugins/openai/llm.py: `_strict_tool_schema: bool = True` (strict tools by default). Checked locally.
- https://platform.openai.com/docs/guides/structured-outputs : strict schemas require `additionalProperties: false` and every property listed.
- https://docs.livekit.io/agents/build/nodes/ : on_user_turn_completed and StopResponse, stt_node override.

Inferred, not measured: the crosstalk attribution caveat (read from the code path, not tested on a live panel).
