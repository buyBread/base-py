import os, logging
from discord.ext import commands

os.system("clear")

print("Starting..", end = "\n\n")

print("Available Extensions:")
for extension in os.listdir("extensions"):
    print(f" -> {extension}")

load_all_extensions = False

print("Extensions to load (Default=All):")
print("==> ", end="")
extensions_list = input()
print() # newline

if extensions_list == "":
    load_all_extensions = True
elif extensions_list.lower() == "all":
    load_all_extensions = True
else:
    extensions_list = extensions_list.split()

bot_client = commands.Bot(command_prefix="!")

for extension in os.listdir("extensions"):
    extension = extension[:-3]
    
    if load_all_extensions:
        bot_client.load_extension(f"extensions.{extension}")
    else:
        if extension in extensions_list:
            bot_client.load_extension(f"extensions.{extension}")

# ugly
bot_client.remove_command("help")

# logging
logger = logging.getLogger("discord")
logger.setLevel(logging.DEBUG)

handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")
handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(name)s: %(message)s'))

logger.addHandler(handler)

# god bless
bot_client.run("")
