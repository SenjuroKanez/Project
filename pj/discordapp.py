import discord.py as dis
import asyncio
def on_message(message):
    if message.content.startswith('!hello'):
        yield from dis.send_message(message.channel, 'Hello World!')
dis.run('email', 'password', on_message)
```

```python
