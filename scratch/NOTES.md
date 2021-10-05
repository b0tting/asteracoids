- Initial project set up (repo, , venv, basic stuff)
- Ik heb een aantal directories toegevoegd: 
	- in /lib zet ik alle python bestanden. Er komt één basale python file in de root
	- in /resource zet ik alles aan graphics en sounds
	- ik heb een werk directory /scratch die ik vol gooi met allerlei losse troep, die zal later wel verdwijnen
	

MVP: 
Story 1: game setup
- We hebben een scherm
- Witte achtergrond

Story 2: Player
- Er staat een ruimtescheepje op het scherm en een rots
- Uitgangspunt: alles dat de rand raakt verschijnt aan de andere kant
- Deze kan draaien met de links en rechts toetsen. De draaisnelheid voor een volle cirkel is ongeveer 2 seconden. 
- Pijl naar voren vliegt het scheepje naar voren. Er zit vertraging in het afnemen van de snelheid. 

Story 3: Asteroid
- Er vliegt een asteroide door het scherm
- Raakt de raket de asteroide, dan stopt het spel

Story 4: Shooting
- Spatie schiet een raketje. Het scheepje schiet per 600ms één raketje
- Raketjes verdwijnen na 2 seconden
- Raakt een raket de asteroide, dan verdwijnen beide. Er verschijnt een nieuw asteroide ergens anders.
