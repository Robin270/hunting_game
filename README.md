# ![Hunting Game Logo](/images/favicon-medium.png) Hunting Game (Beta 0.4.0 Indev documentation)
## Basic info
* Programming languages: Python (PyGame library) [100 %]
* Genre: Platform game
* Current version: Beta v0.4.0 Indev pre-release

## About the game
### General description
A 2D game based on well-known oldschool PC classics. Your goal is to collect 25 gems in 1 minute and 20 seconds without loosing all your 3 lives.

### Game characters
* A player: <img src="images/character.png" alt="A player" width="35px">
* A gem: ![A gem](/images/target.png)
* A bomb: ![A bomb](/images/bomb.png)
* An NPC: <img src="images/npc.png" alt="An NPC" width="35px">

### Controls and basic gameplay
* Once you **click on a "Start" button** in the opening GUI, the timer (1 min 20 sec) starts counting and the **game is running**. The game is based on so called **in-game ticks**, an tick occurs **60 times per second**, so every 60th tick, the timer is updated.
* If you manage to collect **25 gems** before the time runs out, **you win**.
* If you **loose all your lives** or **run out of time** before you collect 25 gems, **you loose**.

##### Character
* You control your **character** on the screen **with arrows** (*supports diagonal movement*).

##### Gems
* On start, the game within the screen **randomly generates one gem and three bombs**. Every time you collect a gem (by just sliding over it with your character), the game generates **a new one** and moves each bomb to a **new random position** within the screen (*the game will never generate a hostile game feature to a player's current position – it checks for that*).

##### Bombs
* Similar behaviour have the **bombs**. But with one important difference, that when you collide with them, you'll **loose one heart** (*you can see your lives in the topleft corner*) and the one particular bomb you collided with again **randomly changes its location** so there are always exactly 3 bombs on the screen.

##### NPC
* Probably the most annoying part of the whole game – **the NPC**. A non-player throwing star-like character that **wanders around the screen** and **deals one heart of damage** when a player accidentaly gets hit by it. **It's unpredictable** – you never know under **what angle and how fast** will it launch towards you from a corner of the screen. After a collision with the NPC, it respawns at a random position and continues behaving the same unpredictable way.

#### Additional features
##### Sprinting and energy bar
* When you need to **quickly move** your character on the screen, you can hold **space bar** to move **1.8 times faster** (*just moving diagonally doesn't make you move faster – it's prevented*).
* You can see your energy bar at the topright corner of the screen.
* The **energy bar** has length of 400 and each tick you're holding down the space bar **it's reduced** by 3. Of course, you have to hold an arrow at the same time as the space bar, otherwise you're wasting energy from your energy bar.
* When you run out of energy, don't worry, **it'll slowly refill** to its full capacity. You just have to put your fingers away from the space bar for a little while. The energy bar refills with the speed of 1 length unit per tick (so 3 times slower than it decreases). When you keep holding down the space bar even when you have already run out of energy, you're just scamming yourself – there's no point in holding that and it blocks refilling the energy.

##### Regeneration
* When you are **low on hearts**, the **regeneration bonus** might come in very handy. It simply **regenerates you one heart** when you collect it.
* When you have **2 hearts remaining**, each tick the game has a **1 in 1600 chance** to generate this bonus **randomly on the screen**.
* When you have only **1 heart left**, each tick the game has a **1 in 950** chance to generate one.
* But the **bonus won't be there forever**. After 150 ticks the **bonus will start warning you by flashing 3 times** that it'll soon despawn.
    * ![A regeneration bonus](/images/heart-regen.png) ![A flashing regeneration bonus](/images/heart-regen-light.png)

## Download instructions
* After you click on the download link, allow your computer to download the file. Installers with .exe extension could be potentialy dangerous, but you can trust this game.
* After downloading the .exe installer, simply enough, run it. You'll probably have to deal with "Windows defended your computer" alert, but just click "More info" and then "Run anyway". Then go through few pages of unneccessary settings (you can set a desktop shortcut etc.) and start the installation. It shouldn't take longer that few seconds.
* And you're ready to play. Enjoy!