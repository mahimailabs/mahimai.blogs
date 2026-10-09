# Sources

- https://github.com/mahimairaja/awesome-voice-apps/tree/main/demos/voice-checkout : agent code quoted in the post (call_page, fill_checkout, place_order, _page_edited, error codes 2001 and 2002, 4 s timeout). Lands with the feat/checkout-demo-4btu93 PR.
- mahimai.ca feat/checkout-demo-4btu93 : the page side quoted in the post (applyFields, orderProblem, registerRpcMethod handlers, page_edited call, pageRpc token grant) in src/components/playground/checkout.ts, CheckoutPanel.tsx and src/server/playground/service.ts.
- https://docs.livekit.io/transport/data/rpc/ : registerRpcMethod and performRpc, 15 KiB payload limit, default 10 s timeout, reserved error codes 1001 to 1999 and the built-in error table.
- https://docs.livekit.io/agents/logic/tools/forwarding/ : forwarding tool calls to the frontend over RPC.
- livekit-agents 1.8.5 source (checked locally): ToolError message is shown to the LLM; RoomOptions(text_input=False) disables the lk.chat text input, which is on by default. livekit-rtc RpcError max message length: the client SDK exposes RpcError.MAX_MESSAGE_BYTES; the post says "a few hundred bytes" and the page clips to 240 characters.
- Inferred, confirm on the first live call: the SFU drops data packets from a participant without canPublishData, so the browser cannot answer RPC on the old mic-only token. The LiveKit RPC docs do not state the permission explicitly.
- Canadian postal code first letters per province and the 2026 sales tax rates (HST 13% ON, 15% Atlantic, QC 14.975% combined, BC and MB 12%, SK 11%, AB and territories 5% GST) are used for the demo store only; the post quotes no rates.

No benchmark numbers, prices or version claims beyond what the linked code pins.
