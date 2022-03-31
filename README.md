# osu-stats
The osu!stats discord bot made in Python using v1 osu API. 

Python 3.8 -> latest (24.03.2022)

Modules:
py-cord==2.0.0b5
aiohttp
python-dotenv

To make the bot work:
1. Clone the repo.
2. Configure bot by creating ".env" file in main bot folder (where main.py is stored)
3. After creating ".env":
    - Copy everything from ".env.example"
    - Replace CHANGEME fields by your tokens.


Bot uses Slash Commands (`applications.commands` scope)

[osu!stats legacy](https://github.com/TheGiga/osu-stats-legacy) (uses default message commands, will not recieve updates)

[Add existing copy of the bot by this link](https://discord.com/api/oauth2/authorize?client_id=804834494486020106&permissions=105227078720&scope=bot%20applications.commands)
