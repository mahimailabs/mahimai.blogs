# Sources

- https://docs.livekit.io/agents/logic/tools/design/ : "Update in place instead of handing off": update_instructions and update_tools on the current agent when only the prompt or tools change.
- https://docs.livekit.io/transport/data/rpc/ : performRpc, registering methods, RpcError for custom errors returned to the caller.
- https://docs.livekit.io/agents/server/agent-dispatch/ : dispatch via access token (RoomAgentDispatch in RoomConfiguration), dispatched when the first participant creates the room.
- livekit-agents 1.8.5 source, livekit/agents/voice/agent.py : Agent.update_instructions and Agent.update_tools docstrings (also update a realtime session when one is running).
- livekit-plugins-cartesia (with livekit-agents 1.8.5), tts.py : TTS.update_options(voice=...); default voice f786b574-daa5-4673-aa0c-cbe3e8534c02 (Katie).
- https://docs.livekit.io/agents/models/tts/inference/cartesia : voice ids for Blake, Jacqueline and Robyn used in the demo.
- https://github.com/mahimairaja/awesome-voice-apps/tree/main/demos/build-your-own-agent : the agent, once the worker PR merges. Hosted adapter and tests in demos/drive-thru-coffee (hosted_builder.py, test_hosted_builder.py).

Not claimed: no swap latency figure. The panel shows the time the worker measured for each swap; publish a number only after measuring it on the live worker.
