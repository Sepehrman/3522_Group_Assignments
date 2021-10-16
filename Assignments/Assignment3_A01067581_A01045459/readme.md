# PokeAPI Command Line Application
A Commandline RESTful API using PokeAPI and usage of Chain of Responsibility Design Pattern to display pokemons' movements, powers, and abilities.

## Installation

1. clone the repo using:
```bash
git clone https://github.com/Sepehrman/3522_Group_Assignments/tree/main/Assignments/Assignment3_A01067581_A01045459
```



## Application Startup
Simply run the program using
```python
python pokedex.py
```

### Use the following argument to receive the details of the application
```python
python pokedex.py --help
```
```bash
optional arguments:
  -h, --help            show this help message and exit
  --mode MODE, -m MODE  Should be either ability, move, or pokemon
  --inputfile INPUTFILE
                        File input needs to be .txt
  --inputdata INPUTDATA [INPUTDATA ...]
                        Input must be name or id
  -o OUTPUT, --output OUTPUT
                        The output of the program. This is 'print' by default, but can be set to a file name as well.
  --expanded            The app will expand the queries if this argument is provided. But will simply print the given data if nothing is given.

```


#### mode of the abilities can be either ability, move, or pokemon to GET the necessary information. We can simply run the program by passing in one specific data input or multiple inputs:
```python
python pokedex.py -m ability --inputdata 5
```


### Which results in:
```bash
Request: Mode: PokedexMode.ABILITY, InputData: ['5'], InputFile: None, Output: print, Expanded: False, QueryData = None, NumberOfRequests None
*** Processing your Pokemon Requests ***

----- Printing to Console -----

Ability Name: sturdy
ID: 5
Generation: generation-iii
Effect: When this Pokémon is at full HP, any hit that would knock it out will instead leave it with 1 HP.  Regardless of its current HP, it is also immune to the one-hit KO moves: fissure, guillotine, horn drill, and sheer cold.

If this Pokémon is holding a focus sash, this ability takes precedence and the item will not be consumed.
Effect (Short): Prevents being KOed from full HP, leaving 1 HP instead.  Protects against the one-hit KO moves regardless of HP.
Pokemon: geodude, graveler, golem, magnemite, magneton, onix, sudowoodo, pineco, forretress, steelix, shuckle, skarmory, donphan, nosepass, aron, lairon, aggron, relicanth, regirock, shieldon, bastiodon, bonsly, magnezone, probopass
, roggenrola, boldore, gigalith, sawk, dwebble, crustle, tirtouga, carracosta, tyrunt, carbink, bergmite, avalugg, togedemaru, cosmoem, geodude-alola, graveler-alola, golem-alola, togedemaru-totem
Is Expanded: False
```



### An Example of Multiple moves with an output to a file would look like:
```python
python pokedex.py -m move --inputdata 1 2 3
```

# Resulting in:
```bash
*** Processing your Pokemon Requests ***

----- Printing to Console -----

ID: 1
Name: pound
Generation: generation-i
Accuracy: 100
PP: 35
Power: 40
Ability Type: normal
Damage: physical
Effect (Short): Inflicts regular damage with no additional effect.
Is Expanded: False


ID: 2
Name: karate-chop
Generation: generation-i
Accuracy: 100
PP: 25
Power: 50
Ability Type: fighting
Damage: physical
Effect (Short): Has an increased chance for a critical hit.
Is Expanded: False


ID: 3
Name: double-slap
Generation: generation-i
Accuracy: 85
PP: 10
Power: 15
Ability Type: normal
Damage: physical
Effect (Short): Hits 2-5 times in one turn.
Is Expanded: False


```




