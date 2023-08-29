#importing from other files
from enemy import *
from weapon import *
from armour import *
from spell import *
from item import *
from upgrade import *

class Room:
    """
    The parent class for a room

    Attributes
    ----------
    - name : str
      Name of the room
    - enemy : Enemy
      The enemy that is in the room
    - description : str
      Description of the room
    - left : Room
      The room on the left
    - right : Room
      The room on the right
    - forward : Room
      The room in front
    - back : Room
      The room to the back
    - been_here : bool
      True if the player has entered the room before, False otherwise
    - loot : Item
      The loot that can be found in the room
    """
   
    def __init__(self):
        self.name = ""
        self.enemy = None
        self.description = ""
        self.left = None
        self.right = None
        self.forward = None
        self.back = None
        self.been_here = False
        self.loot = None
        self.coord = 0
        self.secret = False

    def link_left(self, room):
        room.right = self
        self.left = room

    def link_right(self, room):
        room.left = self
        self.right = room

    def link_forward(self, room):
        room.back = self
        self.forward = room

    def link_back(self, room):
        room.forward = self
        self.back = room
        
class Dirtmouth(Room):
    """
    A room that inherits from the Room class
    """
    
    def __init__(self):
        super().__init__()
        self.enemy = TheRadiance()
        self.name = "Dirtmouth"
        self.description = "You stepped into Dirtmouth, a haunting cliffside town in the depths of Hallownest, standing as a silent sentinel overlooking a dark and mysterious underground world. Its dilapidated buildings and eerie stillness set the tone for your perilous journey"
        self.loot = FlaskOfCrimsonTears()
        
        self.link_left(Midgar())
        self.link_right(HyruleKingdom())
        self.link_forward(TheEndDimension())

class CelestialResort(Room):
    """
    A room that inherits from the Room class
    """
    
    def __init__(self):
        super().__init__()
        self.enemy = MrOshiro()
        self.name = "Celestial Resort"
        self.description = "You stepped into a towering sanctuary of serenity nestled amidst the treacherous slopes of Celeste Mountain, a paradoxical challenge and a refuge for your weary soul. Its elegant halls and perilous puzzles mirrored your personal journey, a delicate dance between inner turmoil and newfound strength."
        self.loot = FlaskOfCeruleanTears()
        
        self.link_back(Ascent())

class TheForge(Room):
    """
    A room that inherits from the Room class
    """
    
    def __init__(self):
        super().__init__()
        self.enemy = TheHighDragun()
        self.name = "The Forge"
        self.description = "You stepped into a blistering hellscape deep within the Gungeon, a relentless crucible where you honed your combat skills to a razor's edge. Its molten rivers and infernal denizens pushed you to your limits, but you are determined to conquer it and uncover the ultimate weapon hidden within."
        self.loot = FlaskOfCrimsonTears()
        
        self.link_forward(Mementos())

class StormveilCastle(Room):
    """
    A room that inherits from the Room class
    """
    
    def __init__(self):
        super().__init__()
        self.enemy = GodrickTheGrafted()
        self.name = "Stormveil Castle"
        self.description = "You stepped into a legacy dungeon, a castle that lies on the cliff of stormveil, littered with hoards of enemies"
        self.loot = FlaskOfCeruleanTears()
        
        self.link_forward(Kamurocho())
        self.link_right(TheHallow())


class ApertureLab(Room):
    """
    A room that inherits from the Room class
    """
    
    def __init__(self):
        super().__init__()
        self.enemy = Glados()
        self.name = "Aperture Lab"
        self.description = "You stepped into a sprawling maze of test chambers filled with menacingly cheery robots and the enigmatic AI, GLaDOS. Your journey through this surreal laboratory is a relentless quest for answers, a desperate struggle to escape its surreal confines and unmask the secrets lurking within."
        self.loot = FlaskOfCrimsonTears()

class Zebes(Room):
    """
    A room that inherits from the Room class
    """
    
    def __init__(self):
        super().__init__()
        self.enemy = Ridley()
        self.name = "Zebes"
        self.description = "You stepped into a hostile and alien world, where you face some of your most harrowing battles against the Space Pirates and their nefarious plans. Its treacherous landscapes, infested with hostile creatures, hide the secrets of the Chozo and your relentless pursuit of justice."
        self.loot = DectusMedallionLeft()

class Bunker(Room):
    """
    A room that inherits from the Room class
    """
    
    def __init__(self):
        super().__init__()
        self.enemy = Emil()
        self.name = "Bunker"
        self.description = "You stepped into a grim sanctuary suspended above the ravaged Earth, both a refuge and a reminder of the relentless war against the machines. you receive orders, grapple with the complexities of your existence, and prepare for the constant struggle to reclaim your planet from the alien invaders."
        self.loot = FlaskOfCrimsonTears()

class Asphodel(Room):
    """
    A room that inherits from the Room class
    """
    
    def __init__(self):
        super().__init__()
        self.enemy = TheBoneHyrda()
        self.name = "Asphodel"
        self.description = "You stepped into a desolate collection of rocky islands amidst a sea of fire beyond Tartarus. You travel between these islands through small bone rafts"
        self.loot = FlaskOfCeruleanTears()
        
        self.link_back(Commencement())
        self.link_forward(GreenhillZone())

        

class KingdomOfKu(Room):
    """
    A room that inherits from the Room class
    """
    
    def __init__(self):
        super().__init__()
        self.enemy = GeneralMugen()
        self.name = "Kingdom of Ku"
        self.description = "You stepped into a nation in Hinoeuma with a long and bloody history of conflict and war. Their enemies numbers many, one among several being the fallen nation of U. It was recently ruled by the aging King Jigo Ku, until a coup removed him from power"
        self.loot = FlaskOfCrimsonTears()
        
        self.link_right(Bunker())
        self.link_forward(Zebes())

class GreenhillZone(Room):
    """
    A room that inherits from the Room class
    """
    
    def __init__(self):
        super().__init__()
        self.enemy = DoctorEggman()
        self.name = "Greenhill Zone"
        self.description = "You stepped into a high-speed playground, a vibrant expanse of lush grass and rolling hills, where you feel most at home. Its loop-de-loops and buzzing animal friends provide the perfect backdrop for your never-ending quest to thwart Dr. Robotnik and collect the precious Chaos Emerald"
        self.loot = FlaskOfCeruleanTears()
        
        self.link_forward(KingdomOfKu())
        self.link_left(TheMushroomKingdom())


class TheHallow(Room):
    """
    A room that inherits from the Room class
    """
    
    def __init__(self):
        super().__init__()
        self.enemy = TheMoonLord()
        self.name = "The Hallow"
        self.description = "You stepped into a radiant but eerie biome, a stark contrast to the darkness that permeates the underground. It's a realm where fantastical creatures and rare resources await, but also a place where you must tread carefully to avoid its relentless and otherworldly foes."
        self.loot = FlaskOfCrimsonTears()
        
        self.link_back(TheObraDinn())

class Commencement(Room):
    """
    A room that inherits from the Room class
    """
    
    def __init__(self):
        super().__init__()
        self.enemy = Mithrix()
        self.name = "Commencement"
        self.description = "You stepped into a large domain located above the shattered breach of Petrichor V's moon. It is ostensibly the desolated seat of Mithrix's power, made up of the shattered remains of four individual sections, emblematic of Mithrix and Providence's tools of creation"
        self.loot = FlaskOfCeruleanTears()
        
        self.link_back(WalledCity99())
        

class Midgar(Room):
    """
    A room that inherits from the Room class
    """
    
    def __init__(self):
        super().__init__()
        self.enemy = Sephiroth()
        self.name = "Midgar"
        self.description = "You stepped into the capital city and power base of the Shinra Electric Power Company in the world of Gaia. your memories of this metropolis are a tangled web of both longing and resentment, forever intertwined with your quest for justice and redemption."
        self.loot = FlaskOfCrimsonTears()
        
        self.link_left(TheForge())


class HyruleKingdom(Room):
    """
    A room that inherits from the Room class
    """
    
    def __init__(self):
        super().__init__()
        self.enemy = Ganondorf()
        self.name = "Hyrule Kingdom"
        self.description = "You stepped into a land steeped in legend and mystique, it is your sacred duty to protect as the Hero of Time. Its vast, rolling landscapes and iconic landmarks are both your home and the canvas upon which your destiny is written as you battle the forces of darkness and seek to rescue Princess Zelda."
        self.loot = FlaskOfCeruleanTears()
        
        self.link_back(CelestialResort())


class TheEndDimension(Room):
    """
    A room that inherits from the Room class
    """
    
    def __init__(self):
        super().__init__()
        self.enemy = TheEnderDragon()
        self.name = "The End Dimension"
        self.description = "You stepped into a dark, space-like dimension consisting of separate islands in the void, made out of end stone. It is inhabited by endermen and shulkers."
        self.loot = FlaskOfCrimsonTears()
    
        self.link_forward(TheShriekingShack())


class Kamurocho(Room):
    """
    A room that inherits from the Room class
    """
    
    def __init__(self):
        super().__init__()
        self.enemy = Shibusawa()
        self.name = "Kamurocho"
        self.description = "You stepped into the nightlife capital of Japan. As Tojo Clan territory, the district is home to many yakuza and is often the setting of large and small-scale disputes between the Tojo Clan and their rivals such as the Omi Alliance, as well as intra-clan conflicts between Tojo subsidiaries"
        self.loot = FlaskOfCeruleanTears()
        
        self.link_forward(Snowdin())


class TowerOfFate(Room):
    """
    A room that inherits from the Room class
    """
    
    def __init__(self):
        super().__init__()
        self.enemy = Enchantress()
        self.name = "Tower of Fate"
        self.description = "You stepped in a looming bastion of darkness and danger, standing as the heart of your perilous journey to save your beloved Shield Knight and the realm from the Enchantress's curse. Its treacherous ascent tests your mettle and resolve, driving you to prove that you am truly a knight worthy of legend."
        self.loot = FlaskOfCrimsonTears()

class ShoresOfNine(Room):
    """
    A room that inherits from the Room class
    """
    
    def __init__(self):
        super().__init__()
        self.enemy = Freya()
        self.name = "Shores of Nine"
        self.description = "You stepped into a realm of Norse myth, it offers a temporary respite from the relentless chaos of your past. You navigate this strange land with your son, Atreus, in search of a new beginning, forging a path toward redemption while battling the threats lurking in these uncharted waters."
        self.loot = FlaskOfCeruleanTears()
        
class Mementos(Room):
    """
    A room that inherits from the Room class
    """
    
    def __init__(self):
        super().__init__()
        self.enemy = Yaldabaoth()
        self.name = "Mementos"
        self.description = "You stepped into a sprawling, ever-changing abyss beneath the city, is where you confront the twisted desires of society's heart. It's a labyrinthine reflection of the collective unconscious, where you as a Phantom Thief embark on a mission to change hearts and expose the hidden darkness that plagues Tokyo."
        self.loot = FlaskOfCrimsonTears()
        
        self.link_right(ShoresOfNine())
        self.link_left(Asphodel())


class Ascent(Room):
    """
    A room that inherits from the Room class
    """
    
    def __init__(self):
        super().__init__()
        self.enemy = Reyna()
        self.name = "Ascent"
        self.description = "You step into a clearing, in the middle of what seems to be a city. Surrounding you are buildings, their appearance reminding you of Ancient Roman Architecture. A skyscraper rises into the sky in the distance, its cold, geometric features clashing with the elegant, smooth lines of the buildings surrounding you. It is only when you turn around that you realise the entire city is several hundred metres above the ground."
        self.loot = FlaskOfCeruleanTears()

        self.link_right(SixthCircleOfHell())


class TheShriekingShack(Room):
    """
    A room that inherits from the Room class
    """
    
    def __init__(self):
        super().__init__()
        self.enemy = Voldemort()
        self.name = "The Shrieking Shack"
        self.description = "You step into a notorious and allegedly haunted building near Hogwarts School, known for its eerie and unsettling reputation as the most haunted building in Britain"
        
        self.loot = FlaskOfCrimsonTears()

class SixthCircleOfHell(Room):
    """
    A room that inherits from the Room class
    """
    
    def __init__(self):
        super().__init__()
        self.enemy = Gabriel()
        self.name = "6th Circle of Hell"
        self.description = "You step into an abandoned church bathed in blood red light. The walls are patterned with the faces of the damned, their expressions contorted in agony, doomed to shriek silently for all eternity. On the far side of the room, a church organ looms over you, an eerie, melancholic melody flowing from its pipes. Its player, a lone figure clad in gold and silver armour"
        self.loot = FlaskOfCeruleanTears()
        
        self.link_forward(StormveilCastle())
        self.link_back(TowerOfFate())

class Snowdin(Room):
    """
    A room that inherits from the Room class
    """
    
    def __init__(self):
        super().__init__()
        self.enemy = Flowey()
        self.name = "Snowdin"
        self.description = "You step into a quaint and snowy town nestled in the underground, itexudes a cozy charm with its warm, dimly lit shops and friendly monster residents. The gentle fall of snowflakes and the sound of crackling fires create a serene atmosphere that contrasts the rest of your journey"
        self.loot = FlaskOfCrimsonTears()
        
        self.link_left(TheAstralPlane())
        self.link_right(TheSealedTemple())
        self.link_forward(ApertureLab())


class TheSealedTemple(Room):
    """
    A room that inherits from the Room class
    """
    
    def __init__(self):
        super().__init__()
        self.enemy = TheHeir()
        self.name = "The Sealed Temple"
        self.description = "You step into a mysterious, ancient structure shrouded in secrecy, holding untold treasures and enigmatic relics waiting to be uncovered by the brave adventurer. Its imposing architecture and mystic aura make it a central point of intrigue and discovery"
        self.loot = DectusMedallionRight()

class TheAstralPlane(Room):
    """
    A room that inherits from the Room class
    """
    
    def __init__(self):
        super().__init__()
        self.enemy = JenaAnderson()
        self.name = "The Astral Plane"
        self.description = "You step into surreal and nightmarish realm that exists parallel to the human world, inhabited by grotesque and otherworldly creatures known as Chimeras"
        self.loot = FlaskOfCrimsonTears()

class TheObraDinn(Room):
    """
    A room that inherits from the Room class
    """
    
    def __init__(self):
        super().__init__()
        self.enemy = TheKraken()
        self.name = "The Obra Dinn"
        self.description = "You step onto a merchant vessel that mysteriously reappeared in 1807 after being lost at sea for five years, with all of its crew either dead or missing"
        self.loot = FlaskOfCeruleanTears()

class TheMushroomKingdom(Room):
    """
    A room that inherits from the Room class
    """
    
    def __init__(self):
        super().__init__()
        self.enemy = Bowser()
        self.name = "The Mushroom Kingdom"
        self.description = "You step into a colorful and enchanting land filled with lush forests, towering mountains, and cheerful inhabitants like Toads and Yoshis"
        self.loot = FlaskOfCrimsonTears()

class WalledCity99(Room):
    """
    A room that inherits from the Room class
    """
    
    def __init__(self):
        super().__init__()
        self.enemy = Sentinel()
        self.name = "Walled City 99"
        self.description = "You step into a dystopian urban enclave characterized by towering, impenetrable walls that isolate its inhabitants from the outside world. Within these walls, a dark and oppressive society unfolds, where the residents are tightly controlled and secrets hide in every shadow"
        self.loot = FlaskOfCrimsonTears()

class TheLastResort(Room):
    """
    A room that inherits from the Room class
    """
    
    def __init__(self):
        super().__init__()
        self.enemy = KingBoo()
        self.name = "The Last Resort"
        self.description = "You step into a sprawling, haunted hotel. This ominous establishment is filled with ghostly inhabitants and puzzles, offering a chilling and atmospheric backdrop"
        self.loot = FlaskOfCrimsonTears()