import os
from discord.ext import commands

os.system("clear")

print("Starting..", end = "\n\n")

print("Available Extensions:")
for extension in os.listdir('extensions'):
    print(f" -> {extension[:-3]}")

extensions_list = []
load_all_extensions = False

print("Extensions to load (Default=all):")
print(" => ", end="")
extensions_to_load = input()
print() # newline

if extensions_to_load == "" or "all":
    load_all_extensions = True
else:
    extensions_list = extensions_to_load.split()

bot_client = commands.Bot(command_prefix="!")

if load_all_extensions:
    for extension in os.listdir("extensions"):
	    bot_client.load_extension(f"extensions.{extension[:-3]}")
else:
    for extension in os.listdir("extensions"):
        if extension in extensions_list:
            bot_client.load_extension(f"extensions.{extension[:-3]}")

# ugly
bot_client.remove_command("help")

# god bless
bot_client.run("")