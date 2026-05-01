from aiohttp import web
from aiohttp_cors import setup as cors_setup, ResourceOptions
from botbuilder.core import ConversationState, MemoryStorage, TurnContext
from botbuilder.core.bot_framework_adapter import BotFrameworkAdapter, BotFrameworkAdapterSettings
from botbuilder.schema import Activity, ConversationAccount, ChannelAccount
from config import DefaultConfig
from bot import ITOpremaBot
import json

CONFIG = DefaultConfig()
MEMORY = MemoryStorage()
CONVERSATION_STATE = ConversationState(MEMORY)
BOT = ITOpremaBot(CONVERSATION_STATE)

SETTINGS = BotFrameworkAdapterSettings("", "")
ADAPTER = BotFrameworkAdapter(SETTINGS)

async def messages(req: web.Request) -> web.Response:
    body = await req.json()
    user_text = body.get("text", "")
    conversation_id = body.get("conversation_id", "default")

    activity = Activity(
        type="message",
        text=user_text,
        channel_id="webchat",
        service_url="http://localhost:3978",
        from_property=ChannelAccount(id="user1", name="Korisnik"),
        recipient=ChannelAccount(id="bot", name="IT Oprema Bot"),
        conversation=ConversationAccount(id=conversation_id),
    )

    response_text = []

    async def bot_callback(turn_context: TurnContext):
        original_send = turn_context.send_activity

        async def capture(activity_or_text):
            text = activity_or_text if isinstance(activity_or_text, str) else getattr(activity_or_text, "text", "")
            if text:
                response_text.append(text)

        turn_context.send_activity = capture
        await BOT.on_turn(turn_context)

    context = TurnContext(ADAPTER, activity)
    await bot_callback(context)

    await CONVERSATION_STATE.save_changes(context)

    return web.Response(
        text=json.dumps({"text": response_text[0] if response_text else ""}),
        content_type="application/json"
    )

async def index(req: web.Request) -> web.Response:
    with open("index.html", "r", encoding="utf-8") as f:
        return web.Response(text=f.read(), content_type="text/html")

app = web.Application()
app.router.add_post("/api/messages", messages)
app.router.add_get("/", index)

cors = cors_setup(app, defaults={
    "*": ResourceOptions(allow_credentials=True, expose_headers="*", allow_headers="*")
})
for route in list(app.router.routes()):
    cors.add(route)

if __name__ == "__main__":
    web.run_app(app, host="localhost", port=CONFIG.PORT)