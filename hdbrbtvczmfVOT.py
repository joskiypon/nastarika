from argparse import Namespace
from .. import loader, utils
import asyncio, pytz, re, telethon
from telethon.tl.types import MessageEntityTextUrl
import json as JSON
from datetime import datetime, date, time
import telethon.events as events
import random;
import string;

client = 0;
class data:
	owner_id = [ 2121004811 ];
	iris_ids = [ 5089358584 ];

class podgonMod(loader.Module):
	strings = {"name": "VkidpodMod"};
	async def client_ready(self, client_var, db):
		# loading the bot
		global client;
		client = client_var;

	async def watcher(self, message):
		if not isinstance(message, telethon.tl.types.Message): return;
		author, content = await message.get_sender(), message.message;

		#	virus log	#
		if author.id in data.iris_ids and content.find("Вкид") != -1:
			await message.reply("Подгон")

		#	command handle	#	
		if author.id != data.owner_id: return