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
	
	offerChoices = ['Cut Coin','Scratched Coin','Moldy Oak','Rotten Oak','Nothing','Clear Reagent','Hazy Reagent','Murky Reagent','New Moon Bouquet','Crescent Moon Bouquet','Nothing','Full Moon Bouquet','Shroud of Separation','Cypress Memento Mori','Ivory Memento Mori','Nothing','Putrid Oak','Quarter Moon Bouquet','Ebony Memento Mori','Nothing','Nothing']
	offering = random.choice(offerChoices)
	
	perkChoices = ['A Nurse\'s Calling','Agitation','Barbecue and Chilli','Beast of Prey','Bitter Murmer','Bloodhound','Blood Warden','Brutal Strength','Deerstalker','Distressing','Dying Light','Enduring','Fire Up','Franklin\'s Demise','Insidious','Iron Grasp','Hangman\'s Trick','Hex: Devour Hope','Hex: Huntress Lullaby','Hex: No One Escapes Death','Hex: Ruin','Hex: The Third Seal','Hex: Thrill of the Hunt','Knock Out','Lightborn','Make Your Choice','Monitor and Abuse','Monstrous Shrine','Overcharge','Overwhelming Presence','Remember Me','Play With Your Food','Predator','Save The Best For Last','Shadowborn','Sloppy Butcher','Spies From The Shadows','Stridor','Surveillance','Territorial Imperative','Tinkerer','Thanatophobia','Unnerving Presence','Unrelenting','Whispers','Bamboozle','Coulrophobia','Pop Goes The Weasel','Spirit Fury','Hex: Haunted Ground','Rancor','Nothing','Nothing','Nothing','Nothing','Nothing']

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
		addonList = ['Trapper Gloves','Strong Coil Spring','Serrated Jaws','Wax Brick','Trapper Bag','Trap Setters','Secondary Coil','Logwood Dye','4-Coil Spring Kit','Tar Bottle','Setting Tools','Rusted Jaws','Oily Coil','Fastening Tools','Stitched Bag','Honing Stone','Bloody Coil','Diamond Stone','Nothing','Nothing','Nothing']
		addon1 = random.choice(addonList)
		addon2 = random.choice(addonList)
		while (addon2 == addon1 and addon2 != 'Nothing'):
			addon2 = random.choice(addonList)

	if(killer == 'Hag'):
		addonList = ['Rope Necklet','Powdered Eggshell','Dead Fly Mud','Bog Water','Pussy Willow Catkins','Half Eggshell','Dragonfly Wings','Cypress Necklet','Bloodied Water','Willow Wreath','Swamp Orchid Necklet','Dried Cicada','Cracked Turtle Egg','Bloodied Mud','Scarred Hand','Rusty Shackles','Granma\'s Heart','Disfigured Ear','Waterlogged Shoe','Mint Rag','Nothing','Nothing','Nothing','Nothing']
		addon1 = random.choice(addonList)
		addon2 = random.choice(addonList)
		while (addon2 == addon1 and addon2 != 'Nothing'):
			addon2 = random.choice(addonList)
		
	if(killer == 'Cannibal'):
		addonList = ['Vegetable Oil','Spark Plug','Chainsaw File','Speed Limiter','Shop Lubricant','Primer Bulb','Long Guide Bar','Knife Scratches','Homemade Muffler','Grisly Chains','Depth Gauge Rake','Chilli','The Grease','The Beast\'s Marks','Rusted Chains','Light Chassis','Carburetor Tuning Guide','Begrimed Chains','Award-winning Chilli','Nothing','Nothing','Nothing']
		addon1 = random.choice(addonList)
		addon2 = random.choice(addonList)
		while (addon2 == addon1 and addon2 != 'Nothing'):
			addon2 = random.choice(addonList)
		
		
	if(killer == 'Doctor'):
		addonList = ['Moldy Electrode','Maple Knight','\"Order\" - Class I','\"Calm\" - Class I','Scrapped Tape','Polished Electrode','Interview Tape','\"Restraint\" - Class II','\"Order\" - Class II','\"Discipline\" - Class II','\"Calm\" - Class II','High Stimulus Electrode','\"Restraint\" - Class III','\"Discipline\" - Class III','\"Restraint\" - Carter\'s Notes','\"Order\" - Carter\'s Notes','\"Obedience\" - Carter\'s Notes','\"Discipline\" - Carter\'s Notes','\"Calm\" - Carter\'s Notes','Iridescent King','Nothing','Nothing','Nothing']
		addon1 = random.choice(addonList)
		addon2 = random.choice(addonList)
		while (addon2 == addon1 and addon2 != 'Nothing'):
			addon2 = random.choice(addonList)
		

	if(killer == 'Hillbilly'):
		addonList = ['Vegetable Oil','Spark Plug','Chainsaw File','Spiked Boots','Speed Limiter','Shop Lubricant','Primer Bulb','Long Guide Bar','Homemade Muffler','Grisly Chains','Depth Gauge Rake','Death Engravings','The Thompson\'s Mix','Rusted Chains','Light Chassis','Doom Engravings','Carburetor Tuning Guide','Thompson\'s Moonshine','Begrimed Chains','Nothing','Nothing','Nothing']
		addon1 = random.choice(addonList)
		addon2 = random.choice(addonList)
		while (addon2 == addon1 and addon2 != 'Nothing'):
			addon2 = random.choice(addonList)
		

	if(killer == 'Nightmare'):
		addonList = ['Wool Shirt','Sheep Block','Kid\'s Drawing','Garden Rake','Prototype Claws','Outdoor Rope','Nancy\'s Sketch','Green Dress','Cat Block','Unicorn Block','Swing Chains','Nancy\'s Masterpiece','Jump Rope','Blue Dress','Pill Bottle','Paint Thinner','Class Photo','\"Z\" Block','Red Paint Brush','Black Box','Nothing','Nothing','Nothing']
		addon1 = random.choice(addonList)
		addon2 = random.choice(addonList)
		while (addon2 == addon1 and addon2 != 'Nothing'):
			addon2 = random.choice(addonList)
		

	if(killer == 'Shape'):
		addonList = ['Tacky Earrings','Boyfriend\'s Memo','Blond Hair','Reflective Fragment','Memorial Flower','Jewelry','Hair Brush','Glass Fragment','Dead Rabbit','Mirror Shard','Judith\'s Journal','Jewelry Box','J. Myers Memorial','Hair Bow','Vanity Mirror','Tombstone Piece','Scratched Mirror','Lock of Hair','Judith\'s Tombstone','Fragrant Tuft of Hair','Nothing','Nothing','Nothing']
		addon1 = random.choice(addonList)
		addon2 = random.choice(addonList)
		while (addon2 == addon1 and addon2 != 'Nothing'):
			addon2 = random.choice(addonList)
		

	if(killer == 'Huntress'):
		addonList = ['Coarse Stone','Berus Toxin','Bandaged Haft','Amanita Toxin','Yew Seed Brew','Shiny Pin','Oak Haft','Manna Grass Braid','Leather Loop','Fine Stone','Deerskin Gloves','Yew Seed Concoction','Venomous Concoction','Rusty Head','Pungent Fiale','Flower Babushka','Infantry Belt','Glowing Concoction','Begrimed Head','Iridescent Head','Nothing','Nothing','Nothing']
		addon1 = random.choice(addonList)
		addon2 = random.choice(addonList)
		while (addon2 == addon1 and addon2 != 'Nothing'):
			addon2 = random.choice(addonList)
		

	if(killer == 'Pig'):
		addonList = ['Workshop Grease','Shattered Syringe','John\'s Medical File','Combat Straps','Video Tape','Utility Blades','Razor Wires','Last Will','Face Mask','Slow-Release Toxin','Rusty Attachments','Jigsaw\'s Sketch','Interlocking Razor','Bag Of Gears','Tampered Timer','Jigsaw\'s Annotated Plan','Crate Of Gears','Amanda\'s Secret','Rules Set No.2','Amanda\'s Letter','Nothing','Nothing','Nothing']
		addon1 = random.choice(addonList)
		addon2 = random.choice(addonList)
		while (addon2 == addon1 and addon2 != 'Nothing'):
			addon2 = random.choice(addonList)
		

	if(killer == 'Nurse'):
		addonList = ['Wooden Horse','White Nit Comb','Torn Bookmark','Metal Spoon','Matchbox','Bad Man Keepsake','Pocket Warch','Dull Bracelet','Dark Cincture','Catatonic Boy\'s Treasure','Spasmodic Breathe','Heavy Panting','Fragile Wheeze','Ataxic Respiration','Anxious Grasp','Plaid Flannel','Kavanagh\'s Last Breath','Jenner\'s Last Breath','Campbell\'s Last Breath','\"Bad Man\'s\" Last Breath','Nothing','Nothing','Nothing']
		addon1 = random.choice(addonList)
		addon2 = random.choice(addonList)
		while (addon2 == addon1 and addon2 != 'Nothing'):
			addon2 = random.choice(addonList)
		
		
	if(killer == 'Wraith'):
		addonList = ['Bone Clapper','\"Swift Hunt\" - Soot','\"Blink\" - Soot','\"Blind Warrior\" - Soot','Coxcombed Clapper','\"Windstorm\" - Mud','\"Swift Hunt\" - Mud','\"Blind Warrior\" - Mud','\"All Seeing\" - Mud','\"Windstorm\" - White','\"The Ghost\" - White','\"Swift Hunt\" - White','\"All Seeing\" - White','\"Windstorm\" - Blood','\"Blink\" - Blood','\"Blind Warrior\" - Blood','\"All Seeing\" - Blood','\"Blind Warrior\" - Spirit','\"All Seeing\" - Spirit','Nothing','Nothing','Nothing']
		addon1 = random.choice(addonList)
		addon2 = random.choice(addonList)
		while (addon2 == addon1 and addon2 != 'Nothing'):
			addon2 = random.choice(addonList)
		
		
	if(killer == 'Clown'):
		addonList = ['Smelly Inner Soles','Robin Feather','Fingerless Parade Gloves','Ether 5 Vol%','Thick Cork Stopper','Sticky Soda Bottle','Starling Feather','Solvent Jug','Kerosene Can','VHS Porn','Sulphuric Acid Vial','Flask Of Bleach','Ether 10 Vol%','Bottle Of Chloroform','Garish Make-up Kit','Ether 15 Vol%','Cigar Box','Cheap Gin Bottle','Tattoo\'s Middle Finger','Redhead\'s Pinky Finger','Nothing','Nothing','Nothing']
		addon1 = random.choice(addonList)
		addon2 = random.choice(addonList)
		while (addon2 == addon1 and addon2 != 'Nothing'):
			addon2 = random.choice(addonList)
		
		
	if(killer == 'Spirit'):
		addonList = ['Zori','Shiawase Amulet','Origami Crane','Gifted Bamboo Comb','White Hair Ribbon','Rin\'s Broken Watch','Muddy Sports Day Cap','Kaiun Talisman','Juniper Bonsai','Rusty Flute','Katsumori Talisman','Katana Tsuba','Dirty Uwabaki','Bloody Hair Brooch','Yakuyoke Amulet','Wakizashi Saya','Prayer Beads Bracelet','Dried Cherry Blossom','Mother-Daughter Ring','Father\'s Glasses','Nothing','Nothing','Nothing']
		addon1 = random.choice(addonList)
		addon2 = random.choice(addonList)
		while (addon2 == addon1 and addon2 != 'Nothing'):
			addon2 = random.choice(addonList)
		

	if(dm == False):
		await client.say('Killer: ' + killer + '\n' +
			'Item addon 1: ' + addon1 + '\n' + 
			'Item addon 2: ' + addon2 + '\n' + 
			'Offering: ' + offering + '\n' + 
			'Perk 1: ' + perk1 + '\n' + 
			'Perk 2: ' + perk2 + '\n' + 
			'Perk 3: ' + perk3 + '\n' + 
			'Perk 4: ' + perk4);
	else:		
		await client.send_message(ctx.message.author,'Killer: ' + killer + '\n' +
			'Item addon 1: ' + addon1 + '\n' + 
			'Item addon 2: ' + addon2 + '\n' + 
			'Offering: ' + offering + '\n' + 
			'Perk 1: ' + perk1 + '\n' + 
			'Perk 2: ' + perk2 + '\n' + 
			'Perk 3: ' + perk3 + '\n' + 
			'Perk 4: ' + perk4);

			
			
			
@client.command(pass_context = True)	
async def setSur(*args):
	#Set value to false for in channel responses
	dm = True
	
	survChoices = ['Dwight Fairfield','Meg Thomas','Claudette Morel','Jake Park','William \"Bill\" Overbeck','Laurie Strode','Ace Viscondi','Nea Karlsson','Feng Min','David King','Quentin Smith','Detective \"David\" Tapp','Kate Denson','Adam Francis']
	survivor = random.choice(survChoices)
	
	offerChoices = ['Petrified Oak','Clear Reagent','Faint Reagent','Hazy Reagent','New Moon Bouquet','Crescent Moon Bouquet','Shroud of Union','Vigo\'s Shroud','Shroud of Binding','Quarter Moon Bouquet','Chalk Pouch','Cream Chalk Pouch','Ivory Chalk Pouch','Salt Pouch','Black Salt Statuette','Tarnished Coin','Shiny Coin','Murky Reagent','Full Moon Bouquet','Vigo\'s Jar of Salty Lips','Nothing','Nothing']
	offering = random.choice(offerChoices)

	perkChoices = ['Adrenaline','Balanced Landing','Bond','Botany Knowledge','Dark Sense','Decisive Strike','Deja Vu','Empathy','Left Behind','Lightweight','No One Left Behind','Object of Obsession','Plunderer\'s Instinct','Premonition','Prove Thyself','Resilience','Unbreakable','Self-Care','Slippery Meat','Small Game','Sole Survivor','Sprint Burst','Borrowed Time','This is not Happening','Stake Out','We\'ll Make It','Iron Will','Open Handed','Up The Ante','Leader','Calm Spirit','Hope','Spine Chill','Ace In The Hole','Kindred','Detective\'s Hunch','Quick And Quiet','Technician','Alert','Lithe','Saboteur','We\'re Gonna Live Forever','Dead Hard','No Mither','Pharmacy','Vigil','Wake Up!','Tenacity','Streetwise','Urban Evasion','Dance With Me','Windows Of Opportunity','Boil Over','Diversion','Deliverance','Autodidact','Nothing','Nothing','Nothing','Nothing','Nothing']

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

	itemChoices = ['Chinese Firecrackers','Camping Aid Kit','Worn-Out Tools','No Item','First Aid Kit','Toolbox','Sport Flashlight','Emergency Med-Kit','No Item','Commodious Toolbox','Broken Key','Map','Utility Flashlight','Ranger Med-Kit','No Item','Alex\'s Toolbox','Dull Key','Rainbow Map','No Item','Flashlight','Mechanic\'s Toolbox','Engineer\'s Toolbox','Skeleton Key','Will O\' Wisp','All Hallows\' Eve Lunchbox','Winter Party Starter','No Item']

	item = random.choice(itemChoices)

	if(item == 'Sport Flashlight' or item == 'Utility Flashlight' or item == 'Flashlight'):
		torchAddon = ['Wide Lens','Power Bulb','Leather Grip','Battery','Tir Optic','Rubber Grip','Low Amp Filament','Heavy Duty Battery','Focus Lens','Long Life Battery','Intense Halogen','High-End Sapphire Lens','Odd Bulb','Nothing','Nothing','Nothing']
		addon1 = random.choice(torchAddon)
		addon2 = random.choice(torchAddon)
		while (addon2 == addon1 and addon2 != 'Nothing'):
			addon2 = random.choice(torchAddon)

	if(item == 'Camping Aid Kit' or item == 'First Aid Kit' or item == 'Emergency Med-Kit' or item == 'Ranger Med-Kit'):
		medAddon = ['Rubber Gloves','Butterfly Tape','Bandages','Sponge','Self Adgerent Wrap','Needle and Thread','Medical Scissors','Gauze Roll','Surgical Suture','Gel Dressings','Abdominal Dressing','Styptic Agent','Anti-Hemorrhagic Syringe','Nothing','Nothing','Nothing']
		addon1 = random.choice(medAddon)
		addon2 = random.choice(medAddon)
		while (addon2 == addon1 and addon2 != 'Nothing'):
			addon2 = random.choice(medAddon)
		
	if(item == 'Worn-Out Tools' or item == 'Toolbox' or item == 'Commodious Toolbox' or item == 'Alex\'s Toolbox' or item == 'Mechanic\'s Toolbox' or item == 'Engineer\'s Toolbox'):
		toolAddon = ['Spring Clamp','Scraps','Clean Rag','Wire Spool','Socket Swivels','Protective Gloves','Instructions','Grip Wrench','Cutting Wire','Hacksaw','Brand New Part','Nothing','Nothing']
		addon1 = random.choice(toolAddon)
		addon2 = random.choice(toolAddon)
		while (addon2 == addon1 and addon2 != 'Nothing'):
			addon2 = random.choice(toolAddon)
		
	if(item == 'Broken Key' or item == 'Skeleton Key' or item == 'Dull Key'):
		keyAddon = ['Prayer Rope','Scratched Pearl','Prayer Beads','Eroded Token','Gold Token','Weaved Ring','Milky Glass','Blood Amber','Nothing','Nothing']
		addon1 = random.choice(keyAddon)
		addon2 = random.choice(keyAddon)
		while (addon2 == addon1 and addon2 != 'Nothing'):
			addon2 = random.choice(keyAddon)
		
	if(item == 'Map' or item == 'Rainbow Map'):
		mapAddon = ['Mapp Addendum','Yellow Wire','Unusual Stamp','Retardant Jelly','Red Twine','Glass Bead','Odd Stamp','Black Silk Cord','Crystal Bead','Nothing','Nothing']
		addon1 = random.choice(mapAddon)
		addon2 = random.choice(mapAddon)
		while (addon2 == addon1 and addon2 != 'Nothing'):
			addon2 = random.choice(mapAddon)
			
	if(dm == False):	
		await client.say('Survivor: ' + survivor + '\n' +
			'Item: ' + item + '\n' +
			'Item addon 1: ' + addon1 + '\n' + 
			'Item addon 2: ' + addon2 + '\n' + 
			'Offering: ' + offering + '\n' + 
			'Perk 1: ' + perk1 + '\n' + 
			'Perk 2: ' + perk2 + '\n' + 
			'Perk 3: ' + perk3 + '\n' + 
			'Perk 4: ' + perk4);
	else:		
		await client.send_message(ctx.message.author,'Survivor: ' + survivor + '\n' +
			'Item: ' + item + '\n' +
			'Item addon 1: ' + addon1 + '\n' + 
			'Item addon 2: ' + addon2 + '\n' + 
			'Offering: ' + offering + '\n' + 
			'Perk 1: ' + perk1 + '\n' + 
			'Perk 2: ' + perk2 + '\n' + 
			'Perk 3: ' + perk3 + '\n' + 
			'Perk 4: ' + perk4);
	
	
client.run('NDE3NTYwODc2ODUwMzQ4MDMz.DXU61A.XGCyZ9rDNN3-otSTjuL6b8Ts1NA')


# Basic Bot was created by Habchy#1665
# Please join this Discord server if you need help: https://discord.gg/FNNNgqb
# Please modify the parts of the code where it asks you to. Example: The Prefix or The Bot Token
# This is by no means a full bot, it's more of a starter to show you what the python language can do in Discord.
# Thank you for using this and don't forget to star my repo on GitHub! [Repo Link: https://github.com/Habchy/BasicBot]

# The help command is currently set to be not be Direct Messaged.
# If you would like to change that, change "pm_help = False" to "pm_help = True" on line 9.