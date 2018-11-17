# These are the dependecies. The bot depends on these to function, hence the name. Please do not change these unless your adding to them, because they can break the bot.
import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform
import random

# Here you can modify the bot's prefix and description and wether it sends help in direct messages or not.
client = Bot(description="Basic Bot prototype", command_prefix="/", pm_help = True)

# This is what happens everytime the bot launches. In this case, it prints information like server count, user count the bot is connected to, and the bot id in the console.
# Do not mess with it because the bot can break, if you wish to do so, please consult me or someone trusted.
@client.event
async def on_ready():
	print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
	print('--------')
	print('Current Discord.py Version: {} | Current Python Version: {}'.format(discord.__version__, platform.python_version()))
	print('--------')
	print('Use this link to invite {}:'.format(client.user.name))
	print('https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8'.format(client.user.id))
	print('--------')
	print('Created by Habchy#1665')
	return await client.change_presence(game=discord.Game(name='PM /setSur and /setKill')) #This is buggy, let us know if it doesn't work.

@client.command(pass_context = True)
async def setKill(ctx):
	#Set value to false for in channel responses
	dm = True
	
	killChoices = ['Trapper','Wraith','Hillbilly','Nurse','Shape','Doctor','Huntress','Cannibal','Nightmare','Pig','Hag','Clown','Spirit']
	killer = random.choice(killChoices)	
	
	offerChoices = ['Clear Reagent (Brown)',
		'Scratched Coin (Yellow)','Moldy Oak (Yellow)','Hazy Reagent (Yellow)','Shroud of Separation (Yellow)','Cypress Memento Mori (Yellow)',
		'Ivory Memento Mori (Green)','Rotten Oak (Green)',
		'Cut Coin (Purple)','Murky Reagent (Purple)','Putrid Oak (Purple)',
		'Ebony Memento Mori (Red)',
		'Nothing','Nothing']
	offering = random.choice(offerChoices)
	
	perkChoices = ['Unnerving Presence (Green)','Brutal Strength (Purple)','Agitation (Purple)', #Trapper
		'Predator (Green)','Bloodhound (Purple)','Shadowborn (Purple)', #Wraith
		'Enduring (Green)','Lightborn (Purple)','Tinkerer (Purple)', #Hillbilly
		'Stridor (Green)','Thanatophobia (Purple)','A Nurse\'s Calling (Purple)', #Nurse
		'Beast of Prey (Green)','Territorial Imperative (Purple)','Hex: Huntress Lullaby (Purple)', #Huntress
		'Save The Best For Last (Purple)','Play With Your Food (Purple)','Dying Light (Purple)', #Shape
		'Hex: The Third Seal (Purple)','Hex: Ruin (Purple)','Hex: Devour Hope (Purple)', #Hag
		'Knock Out (Green)','Barbecue & Chilli (Purple)','Franklin\'s Demise (Purple)', #Cannibal
		'Overwhelming Presence (Green)','Monitor & Abuse (Purple)','Overcharge (Purple)', #Doctor
		'Fire Up (Green)','Remember Me (Purple)','Blood Warden (Purple)', #Nightmare
		'Hangman\'s Trick (Green)','Surveillance (Purple)','Make Your Choice (Purple)', #Pig
		'Bamboozle (Green)','Coulrophobia (Purple)','Pop Goes The Weasel (Purple)', #Clown
		'Spirit Fury (Green)','Hex: Haunted Ground (Purple)','Rancor (Purple)', #Spirit
		'Bitter Murmer (Purple)','Deerstalker (Green)','Distressing (Green)','Insidious (Purple)','Iron Grasp (Green)','Hex: No One Escapes Death (Purple)','Hex: Thrill Of The Hunt (Green)','Monstrous Shrine (Green)','Sloppy Butcher (Green)','Spies From The Shadows (Green)','Unrelenting (Green)','Whispers (Purple)']

	perk1 = random.choice(perkChoices)
	
	perk2 = random.choice(perkChoices)
	while (perk2 == perk1 and perk2 != 'Nothing'):
		perk2 = random.choice(perkChoices)
	
	perk3 = random.choice(perkChoices)
	while(perk3 == perk2 and perk3 != 'Nothing' or perk3 == perk1 and perk3 != 'Nothing'):
		perk3 = random.choice(perkChoices)
	
	perk4 = random.choice(perkChoices)
	while(perk4 == perk3 and perk4 != 'Nothing' or perk4 == perk2 and perk4 != 'Nothing' or perk4 == perk1 and perk4 != 'Nothing' ):
		perk4 = random.choice(perkChoices)
	

	if(killer == 'Trapper'):
		addonList = ['Trapper Sack (Brown)','Trapper Gloves (Brown)','Strong Coil Spring (Brown)','Padded Jaws (Brown)',
			'Trapper Bag (Yellow)','Trap Setters (Yellow)','Serrated Jaws (Yellow)','Logwood Dye (Yellow)','4-Coil Spring Kit (Yellow)',
			'Wax Brick (Green)','Tar Bottle (Green)','Setting Tools (Green)','Secondary Coil (Green)','Rusted Jaws (Green)',
			'Stiched Bag (Purple)','Oily Coil (Purple)','Honing Stone (Purple)','Fastening Tools (Purple)','Iridescent Stone (Red)','Bloody Coil (Red)',
			'Nothing','Nothing','Nothing']
		addon1 = random.choice(addonList)
		addon2 = random.choice(addonList)
		while (addon2 == addon1 and addon2 != 'Nothing'):
			addon2 = random.choice(addonList)

	if(killer == 'Hag'):
		addonList = ['Rope Necklet (Brown)','Powdered Eggshell (Brown)','Dead Fly Mud (Brown)','Bog Water (Brown)',
			'Pussy Willow Catkins (Yellow)','Half Eggshell (Yellow)','Dragonfly Wings (Yellow)','Cypress Necklet (Yellow)','Bloodied Water (Yellow)',
			'Willow Wreath (Green)','Swamp Orchid Necklet (Green)','Dried Cicada (Green)','Cracked Turtle Egg (Green)','Bloodied Mud (Green)',
			'Scarred Hand (Purple)','Rusty Shackles (Purple)','Granma\'s Heart (Purple)','Disfigured Ear (Purple)',
			'Waterlogged Shoe (Red)','Mint Rag (Red)',
			'Nothing','Nothing','Nothing']
		addon1 = random.choice(addonList)
		addon2 = random.choice(addonList)
		while (addon2 == addon1 and addon2 != 'Nothing'):
			addon2 = random.choice(addonList)
		
	if(killer == 'Cannibal'):
		addonList = ['Vegetable Oil (Brown)','Spark Plug (Brown)','Chainsaw File (Brown)',
			'Speed Limiter (Yellow)','Shop Lubricant (Yellow)','Primer Bulb (Yellow)','Long Guide Bar (Yellow)','Knife Scratches (Yellow)','Homemade Muffler (Yellow)','Grisly Chains (Yellow)','Depth Gauge Rake (Yellow)','Chilli (Yellow)',
			'The Grease (Green)','The Beast\'s Marks (Green)','Rusted Chains (Green)','Light Chassis (Green)','Carburettor Tuning Guide (Green)',
			'Begrimed Chains (Purple)','Award-winning Chilli (Purple)',
			'Nothing','Nothing','Nothing']
		addon1 = random.choice(addonList)
		addon2 = random.choice(addonList)
		while (addon2 == addon1 and addon2 != 'Nothing'):
			addon2 = random.choice(addonList)
		
		
	if(killer == 'Doctor'):
		addonList = ['Moldy Electrode (Brown)','Maple Knight (Brown)','\"Order\" - Class I (Brown)','\"Calm\" - Class I (Brown)',
			'Scrapped Tape (Yellow)','Polished Electrode (Yellow)','Interview Tape (Yellow)','\"Restraint\" - Class II (Yellow)','\"Order\" - Class II (Yellow)','\"Discipline\" - Class II (Yellow)','\"Calm\" - Class II (Yellow)',
			'High Stimulus Electrode (Green)','\"Restraint\" - Class III (Green)','\"Discipline\" - Class III (Green)',
			'\"Restraint\" - Carter\'s Notes (Purple)','\"Order\" - Carter\'s Notes (Purple)','\"Obedience\" - Carter\'s Notes (Purple)','\"Discipline\" - Carter\'s Notes (Purple)','\"Calm\" - Carter\'s Notes (Purple)',
			'Iridescent King (Red)',
			'Nothing','Nothing','Nothing']
		addon1 = random.choice(addonList)
		addon2 = random.choice(addonList)
		while (addon2 == addon1 and addon2 != 'Nothing'):
			addon2 = random.choice(addonList)
		

	if(killer == 'Hillbilly'):
		addonList = ['Vegetable Oil (Brown)','Spark Plug (Brown)','Chainsaw File (Brown)',
			'Spiked Boots (Yellow)','Speed Limiter (Yellow)','Shop Lubricant (Yellow)','Primer Bulb (Yellow)','Long Guide Bar (Yellow)','Homemade Muffler (Yellow)','Grisly Chains (Yellow)','Depth Gauge Rake (Yellow)','Death Engravings (Yellow)',
			'The Thompson\'s Mix (Green)','Rusted Chains (Green)','Light Chassis (Green)','Doom Engravings (Green)','Carburetor Tuning Guide (Green)',
			'Thompson\'s Moonshine (Purple)','Begrimed Chains (Purple)',
			'Nothing','Nothing','Nothing']
		addon1 = random.choice(addonList)
		addon2 = random.choice(addonList)
		while (addon2 == addon1 and addon2 != 'Nothing'):
			addon2 = random.choice(addonList)
		

	if(killer == 'Nightmare'):
		addonList = ['Wool Shirt (Brown)','Sheep Block (Brown)','Kid\'s Drawing (Brown)','Garden Rake (Brown)',
			'Prototype Claws (Yellow)','Outdoor Rope (Yellow)','Nancy\'s Sketch (Yellow)','Green Dress (Yellow)','Cat Block (Yellow)',
			'Unicorn Block (Green)','Swing Chains (Green)','Nancy\'s Masterpiece (Green)','Jump Rope (Green)','Blue Dress (Green)',
			'Pill Bottle (Purple)','Paint Thinner (Purple)','Class Photo (Purple)','\"Z\" Block (Purple)',
			'Red Paint Brush (Red)','Black Box (Red)',
			'Nothing','Nothing','Nothing']
		addon1 = random.choice(addonList)
		addon2 = random.choice(addonList)
		while (addon2 == addon1 and addon2 != 'Nothing'):
			addon2 = random.choice(addonList)
		

	if(killer == 'Shape'):
		addonList = ['Tacky Earrings (Brown)','Boyfriend\'s Memo (Brown)','Blond Hair (Brown)',
			'Reflective Fragment (Yellow)','Memorial Flower (Yellow)','Jewelry (Yellow)','Hair Brush (Yellow)','Glass Fragment (Yellow)','Dead Rabbit (Yellow)',
			'Mirror Shard (Green)','Judith\'s Journal (Green)','Jewelry Box (Green)','J. Myers Memorial (Green)','Hair Bow (Green)',
			'Vanity Mirror (Purple)','Tombstone Piece (Purple)','Scratched Mirror (Purple)','Lock of Hair (Purple)',
			'Judith\'s Tombstone (Red)','Fragrant Tuft of Hair (Red)',
			'Nothing','Nothing','Nothing']
		addon1 = random.choice(addonList)
		addon2 = random.choice(addonList)
		while (addon2 == addon1 and addon2 != 'Nothing'):
			addon2 = random.choice(addonList)
		

	if(killer == 'Huntress'):
		addonList = ['Coarse Stone (Brown)','Berus Toxin (Brown)','Bandaged Haft (Brown)','Amanita Toxin (Brown)',
			'Yew Seed Brew (Yellow)','Shiny Pin (Yellow)','Oak Haft (Yellow)','Manna Grass Braid (Yellow)','Leather Loop (Yellow)','Fine Stone (Yellow)','Deerskin Gloves (Yellow)',
			'Yew Seed Concoction (Green)','Venomous Concoction (Green)','Rusty Head (Green)','Pungent Fiale (Green)','Flower Babushka (Green)',
			'Infantry Belt (Purple)','Glowing Concoction (Purple)','Begrimed Head (Purple)',
			'Iridescent Head (Red)',
			'Nothing','Nothing','Nothing']
		addon1 = random.choice(addonList)
		addon2 = random.choice(addonList)
		while (addon2 == addon1 and addon2 != 'Nothing'):
			addon2 = random.choice(addonList)
		

	if(killer == 'Pig'):
		addonList = ['Workshop Grease (Brown)','Shattered Syringe (Brown)','John\'s Medical File (Brown)','Combat Straps (Brown)',
			'Video Tape (Yellow)','Utility Blades (Yellow)','Razor Wires (Yellow)','Last Will (Yellow)','Face Mask (Yellow)',
			'Slow-Release Toxin (Green)','Rusty Attachments (Green)','Jigsaw\'s Sketch (Green)','Interlocking Razor (Green)','Bag Of Gears (Green)',
			'Tampered Timer (Purple)','Jigsaw\'s Annotated Plan (Purple)','Crate Of Gears (Purple)','Amanda\'s Secret (Purple)',
			'Rules Set No.2 (Red)','Amanda\'s Letter (Red)',
			'Nothing','Nothing','Nothing']
		addon1 = random.choice(addonList)
		addon2 = random.choice(addonList)
		while (addon2 == addon1 and addon2 != 'Nothing'):
			addon2 = random.choice(addonList)
		

	if(killer == 'Nurse'):
		addonList = ['Wooden Horse (Brown)','White Nit Comb (Brown)','Torn Bookmark (Brown)','Metal Spoon (Brown)','Matchbox (Brown)','Bad Man Keepsake (Brown)',
			'Pocket Warch (Yellow)','Dull Bracelet (Yellow)','Dark Cincture (Yellow)','Catatonic Boy\'s Treasure (Yellow)',
			'Spasmodic Breathe (Green)','Heavy Panting (Green)','Fragile Wheeze (Green)','Ataxic Respiration (Green)','Anxious Grasp (Green)',
			'Plaid Flannel (Purple)','Kavanagh\'s Last Breath (Purple)','Jenner\'s Last Breath (Purple)','Campbell\'s Last Breath (Purple)','\"Bad Man\'s\" Last Breath (Purple)',
			'Nothing','Nothing','Nothing']
		addon1 = random.choice(addonList)
		addon2 = random.choice(addonList)
		while (addon2 == addon1 and addon2 != 'Nothing'):
			addon2 = random.choice(addonList)
		
		
	if(killer == 'Wraith'):
		addonList = ['\"The Serpent\" - Soot (Brown)','\"The Hound\" - Soot (Brown)','\"The Ghost\" - Soot (Brown)','\"The Beast\" - Soot (Brown)',
			'Bone Clapper (Yellow)','\"Blink\" - Mud (Yellow)','\"Windstorm\" - Mud (Yellow)','\"Swift Hunt\" - Mud (Yellow)','\"Blind Warrior\" - Mud (Yellow)',
			'\"Windstorm\" - White (Green)','\"Swift Hunt\" - White (Green)','\"Shadow Dance\" - White (Green)','\"Blink\" - White (Green)','\"Blind Warrior\" - White (Green)',
			'\"Windstorm\" - Blood (Purple)','\"Swift Hunt\" - Blood (Purple)','\"Shadow Dance\" - Blood (Purple)','\"All Seeing\" - Blood (Purple)',
			'Coxcombed Clapper (Red)','\"All Seeing\" - Spirit (Red)',
			'Nothing','Nothing','Nothing']
		addon1 = random.choice(addonList)
		addon2 = random.choice(addonList)
		while (addon2 == addon1 and addon2 != 'Nothing'):
			addon2 = random.choice(addonList)
		
		
	if(killer == 'Clown'):
		addonList = ['Smelly Inner Soles (Brown)','Robin Feather (Brown)','Fingerless Parade Gloves (Brown)','Ether 5 Vol% (Brown)',
			'Thick Cork Stopper (Yellow)','Sticky Soda Bottle (Yellow)','Starling Feather (Yellow)','Solvent Jug (Yellow)','Kerosene Can (Yellow)'
			,'VHS Porn (Green)','Sulphuric Acid Vial (Green)','Flask Of Bleach (Green)','Ether 10 Vol% (Green)','Bottle Of Chloroform (Green)',
			'Garish Make-up Kit (Purple)','Ether 15 Vol% (Purple)','Cigar Box (Purple)','Cheap Gin Bottle (Purple)',
			'Tattoo\'s Middle Finger (Red)','Redhead\'s Pinky Finger (Red)',
			'Nothing','Nothing','Nothing']
		addon1 = random.choice(addonList)
		addon2 = random.choice(addonList)
		while (addon2 == addon1 and addon2 != 'Nothing'):
			addon2 = random.choice(addonList)
		
		
	if(killer == 'Spirit'):
		addonList = ['Zori (Brown)','Shiawase Amulet (Brown)','Origami Crane (Brown)','Gifted Bamboo Comb (Brown)',
		'White Hair Ribbon (Yellow)','Rin\'s Broken Watch (Yellow)','Muddy Sports Day Cap (Yellow)','Kaiun Talisman (Yellow)','Juniper Bonsai (Yellow)',
		'Rusty Flute (Green)','Katsumori Talisman (Green)','Katana Tsuba (Green)','Dirty Uwabaki (Green)','Bloody Hair Brooch (Green)',
		'Yakuyoke Amulet (Purple)','Wakizashi Saya (Purple)','Prayer Beads Bracelet (Purple)','Dried Cherry Blossom (Purple)',
		'Mother-Daughter Ring (Red)','Father\'s Glasses (Red)',
		'Nothing','Nothing','Nothing']
		addon1 = random.choice(addonList)
		addon2 = random.choice(addonList)
		while (addon2 == addon1 and addon2 != 'Nothing'):
			addon2 = random.choice(addonList)
		

	if(dm == False):
		await client.say('```Killer: ' + killer + '\n' +
			'----------------------------------------' + '\n' +
			'Item addon 1: ' + addon1 + '\n' + 
			'Item addon 2: ' + addon2 + '\n' + 
			'----------------------------------------' + '\n' +
			'Offering: ' + offering + '\n' + 
			'----------------------------------------' + '\n' +
			'Perk 1: ' + perk1 + '\n' + 
			'Perk 2: ' + perk2 + '\n' + 
			'Perk 3: ' + perk3 + '\n' + 
			'Perk 4: ' + perk4 + '\n```');
	else:		
		await client.send_message(ctx.message.author,'```Killer: ' + killer + '\n' +
			'----------------------------------------' + '\n' +
			'Item addon 1: ' + addon1 + '\n' + 
			'Item addon 2: ' + addon2 + '\n' + 
			'----------------------------------------' + '\n' +
			'Offering: ' + offering + '\n' + 
			'----------------------------------------' + '\n' +
			'Perk 1: ' + perk1 + '\n' + 
			'Perk 2: ' + perk2 + '\n' + 
			'Perk 3: ' + perk3 + '\n' + 
			'Perk 4: ' + perk4 + '```');



@client.command(pass_context = True)	
async def setSur(ctx):
	#Set value to false for in channel responses
	dm = True
	
	survChoices = ['Dwight Fairfield','Meg Thomas','Claudette Morel','Jake Park','William \"Bill\" Overbeck','Laurie Strode','Ace Visconti','Nea Karlsson','Feng Min','David King','Quentin Smith','Detective \"David\" Tapp','Kate Denson','Adam Francis']
	survivor = random.choice(survChoices)
	
	offerChoices = ['Clear Reagent (Brown)','Faint Reagent (Brown)','Chalk Pouch (Brown)',
		'Hazy Reagent (Yellow)','Shroud of Union (Yellow)','Vigo\'s Shroud (Yellow)','Cream Chalk Pouch (Yellow)','Salt Pouch (Yellow)','Tarnished Coin (Yellow)',
		'Ivory Chalk Pouch (Green)','Black Salt Statuette (Green)',
		'Shroud of Binding (Purple)','Petrified Oak (Purple)','Shiny Coin (Purple)','Murky Reagent (Purple)','Vigo\'s Jar of Salty Lips (Purple)',
		'Nothing','Nothing']
	offering = random.choice(offerChoices)
	
	perkChoices = ['Bond (Green)','Prove Thyself (Purple)','Leader (Purple)', #Dwight
		'Quick & Quiet (Green)','Sprint Burst (Purple)','Adrenaline (Purple)', #Meg
		'Empathy (Green)','Botany Knowledge (Purple)','Self Care (Purple)', #Claudette
		'Iron Will (Green)','Calm Spirit (Purple)','Saboteur (Purple)', #Jake
		'Balanced Landing (Green)','Urban Evasion (Purple)','Streetwise (Purple)', #Nea
		'Left Behind (Green)','Borrowed Time (Purple)','Unbreakable (Purple)', #Bill
		'We\'re Gonna Live Forever (Green)','Dead Hard (Purple)','No Mither (Purple)', #David King
		'Sole Survivor','Object Of Obsession (Purple)','Decisive Strike (Purple)', #Laurie
		'Open-Handed','Up The Ante (Purple)','Ace In The Hole (Purple)', #Ace
		'Technician (Green)','Lithe (Purple)','Alert (Purple)', #Feng
		'Wake Up! (Green)','Pharmacy (Purple)','Vigil (Purple)', #Quentin
		'Tenacity (Green)','Detective\'s Hunch (Purple)','Stake Out (Purple)', #David Tapp
		'Dance With Me (Purple)','Windows Of Opportunity (Green)','Boil Over (Purple)', #Kate
		'Diversion (Green)','Deliverance (Purple)','Autodidact (Purple)', #Adam
		'Dark Sense (Purple)','Deja Vu (Purple)','Hope (Purple)','Kindred (Purple)','Lightweight (Green)','No One Left Behind (Purple)','Plunderer\'s Instinct (Green)','Premonition (Purple)','Resilience (Purple)','Slippery Meat (Green)','Small Game (Green)','Spine Chill (Purple)','This Is Not Happening (Purple)','We\'ll Make It (Purple)']
	

	perk1 = random.choice(perkChoices)
	
	perk2 = random.choice(perkChoices)
	while (perk2 == perk1 and perk2 != 'Nothing'):
		perk2 = random.choice(perkChoices)
		
	perk3 = random.choice(perkChoices)
	while(perk3 == perk2 and perk3 != 'Nothing' or perk3 == perk1 and perk3 != 'Nothing'):
		perk3 = random.choice(perkChoices)
		
	perk4 = random.choice(perkChoices)
	while(perk4 == perk3 and perk4 != 'Nothing' or perk4 == perk2 and perk4 != 'Nothing' or perk4 == perk1 and perk4 != 'Nothing' ):
		perk4 = random.choice(perkChoices)

	itemChoices = ['Camping Aid Kit (Brown)','Worn-Out Tools (Brown)',
		'First Aid Kit (Yellow)','Toolbox (Yellow)','Flashlight (Yellow)',
		'Emergency Med-Kit (Green)','Commodious Toolbox (Green)','Mechanic\'s Toolbox (Green)','Sport Flashlight (Green)','Broken Key (Green)','Map (Green)',
		'Ranger Med-Kit (Purple)','Alex\'s Toolbox (Purple)','Engineer\'s Toolbox (Purple)','Utility Flashlight (Purple)','Dull Key (Purple)',
		'Skeleton Key (Red)','Rainbow Map (Red)',
		'All Hallows\' Eve Lunchbox (Event)','Chinese Firecrackers (Event)','Winter Party Starter (Event)','Will O\' Wisp (Event)',
		'No Item','No Item','No Item','No Item']

	item = random.choice(itemChoices)

	if(item == 'Flashlight (Yellow)' or item =='Sport Flashlight (Green)' or item == 'Utility Flashlight (Purple)' or item ==  'Will O\' Wisp (Event)'):
		torchAddon = ['Wide Lens (Brown)','Power Bulb (Brown)','Leather Grip (Brown)','Battery (Brown)',
			'Tir Optic (Yellow)','Rubber Grip (Yellow)','Low Amp Filament (Yellow)','Heavy Duty Battery (Yellow)','Focus Lens (Yellow)',
			'Long Life Battery (Green)','Intense Halogen (Green)',
			'High-End Sapphire Lens (Purple)',
			'Odd Bulb (Red)',
			'Nothing','Nothing','Nothing']
		addon1 = random.choice(torchAddon)
		addon2 = random.choice(torchAddon)
		while (addon2 == addon1 and addon2 != 'Nothing'):
			addon2 = random.choice(torchAddon)

	if(item == 'Camping Aid Kit (Brown)' or item == 'First Aid Kit (Yellow)' or item == 'Emergency Med-Kit (Green)' or item == 'Ranger Med-Kit (Purple)' or item == 'All Hallows\' Eve Lunchbox (Event)'):
		medAddon = ['Rubber Gloves (Brown)','Butterfly Tape (Brown)','Bandages (Brown)',
			'Sponge (Yellow)','Self Adgerent Wrap (Yellow)','Needle and Thread (Yellow)','Medical Scissors (Yellow)','Gauze Roll (Yellow)',
			'Surgical Suture (Green)','Gel Dressings (Green)','Abdominal Dressing (Green)',
			'Styptic Agent (Purple)',
			'Anti-Hemorrhagic Syringe (Red)',
			'Nothing','Nothing','Nothing']
		addon1 = random.choice(medAddon)
		addon2 = random.choice(medAddon)
		while (addon2 == addon1 and addon2 != 'Nothing'):
			addon2 = random.choice(medAddon)
		
	if(item == 'Worn-Out Tools (Brown)' or item == 'Toolbox (Yellow)' or item == 'Commodious Toolbox (Green)' or item == 'Mechanic\'s Toolbox (Green)' or item == 'Alex\'s Toolbox (Purple)' or item == 'Engineer\'s Toolbox (Purple)'):
		toolAddon = ['Spring Clamp (Brown)','Scraps (Brown)','Clean Rag (Brown)',
			'Wire Spool (Yellow)','Socket Swivels (Yellow)','Protective Gloves (Yellow)','Instructions (Yellow)', 'Grip	Wrench (Yellow)','Cutting Wire (Yellow)',
			'Hacksaw (Green)','Brand New Part (Red)',
			'Nothing','Nothing','Nothing']
		addon1 = random.choice(toolAddon)
		addon2 = random.choice(toolAddon)
		while (addon2 == addon1 and addon2 != 'Nothing'):
			addon2 = random.choice(toolAddon)
		
	if(item == 'Broken Key (Green)' or item == 'Dull Key (Purple)' or item == 'Skeleton Key (Red)'):
		keyAddon = ['Prayer Rope (Brown)',
			'Scratched Pearl (Yellow)','Prayer Beads (Yellow)','Eroded Token (Yellow)',
			'Gold Token (Green)',
			'Weaved Ring (Purple)','Milky Glass (Purple)','Blood Amber (Purple)',
			'Nothing','Nothing','Nothing']
		addon1 = random.choice(keyAddon)
		addon2 = random.choice(keyAddon)
		while (addon2 == addon1 and addon2 != 'Nothing'):
			addon2 = random.choice(keyAddon)
		
	if(item == 'Map (Green)' or item == 'Rainbow Map (Red)'):
		mapAddon = ['Map Addendum (Brown)',
			'Yellow Wire (Yellow)','Unusual Stamp (Yellow)','Retardant Jelly (Yellow)','Red Twine (Yellow)','Glass Bead (Yellow)',
			'Odd Stamp (Green)','Black Silk Cord (Green)','Crystal Bead (Purple)',
			'Nothing','Nothing','Nothing']
		addon1 = random.choice(mapAddon)
		addon2 = random.choice(mapAddon)
		while (addon2 == addon1 and addon2 != 'Nothing'):
			addon2 = random.choice(mapAddon)
			
		
	if(dm == False):
		if(item == 'No Item'):
			await client.say('```Survivor: ' + survivor + '\n' +
				'----------------------------------------' + '\n' +
				'Item: ' + item + '\n' +
				'----------------------------------------' + '\n' +
				'Offering: ' + offering + '\n' + 
				'----------------------------------------' + '\n' +
				'Perk 1: ' + perk1 + '\n' + 
				'Perk 2: ' + perk2 + '\n' + 
				'Perk 3: ' + perk3 + '\n' + 
				'Perk 4: ' + perk4 + '```');
		else:
			await client.say('```Survivor: ' + survivor + '\n' +
				'----------------------------------------' + '\n' +
				'Item: ' + item + '\n' +
				'Item addon 1: ' + addon1 + '\n' + 
				'Item addon 2: ' + addon2 + '\n' + 
				'----------------------------------------' + '\n' +
				'Offering: ' + offering + '\n' + 
				'----------------------------------------' + '\n' +
				'Perk 1: ' + perk1 + '\n' + 
				'Perk 2: ' + perk2 + '\n' + 
				'Perk 3: ' + perk3 + '\n' + 
				'Perk 4: ' + perk4 + '```');
	else:
		if(item == 'No Item'):
			await client.send_message(ctx.message.author,'```Survivor: ' + survivor + '\n' +
				'----------------------------------------' + '\n' +
				'Item: ' + item + '\n' +
				'----------------------------------------' + '\n' +
				'Offering: ' + offering + '\n' + 
				'----------------------------------------' + '\n' +
				'Perk 1: ' + perk1 + '\n' + 
				'Perk 2: ' + perk2 + '\n' + 
				'Perk 3: ' + perk3 + '\n' + 
				'Perk 4: ' + perk4 + '```');
		else:
			await client.send_message(ctx.message.author,'```Survivor: ' + survivor + '\n' +
				'----------------------------------------' + '\n' +
				'Item: ' + item + '\n' +
				'Item addon 1: ' + addon1 + '\n' + 
				'Item addon 2: ' + addon2 + '\n' + 
				'----------------------------------------' + '\n' +
				'Offering: ' + offering + '\n' + 
				'----------------------------------------' + '\n' +
				'Perk 1: ' + perk1 + '\n' + 
				'Perk 2: ' + perk2 + '\n' + 
				'Perk 3: ' + perk3 + '\n' + 
				'Perk 4: ' + perk4 + '```');
	
	
client.run('NDE3NTYwODc2ODUwMzQ4MDMz.DXU61A.XGCyZ9rDNN3-otSTjuL6b8Ts1NA')


# Basic Bot was created by Habchy#1665
# Please join this Discord server if you need help: https://discord.gg/FNNNgqb
# Please modify the parts of the code where it asks you to. Example: The Prefix or The Bot Token
# This is by no means a full bot, it's more of a starter to show you what the python language can do in Discord.
# Thank you for using this and don't forget to star my repo on GitHub! [Repo Link: https://github.com/Habchy/BasicBot]

# The help command is currently set to be not be Direct Messaged.
# If you would like to change that, change "pm_help = False" to "pm_help = True" on line 9.