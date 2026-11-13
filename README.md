# Other5ForestBiome_Minimal

A small forest for Other5 Creations: two forest maps (`Maps/Forest`, `Maps/Forest_Partition`), stylized oak, birch and pine trees
and bushes (Cozy Nature, a small free Fab pack), forest-floor ground, and two game modes (`BP_Other5CombatGameMode`, `BP_Other5ThirdPersonGameMode`).

## Stand-in art, and how to get the real art
The trees and bushes come from **Cozy Nature** (ATRV Studio, free on Fab); the ground and sky materials are Other5's
own, using Cozy Nature's grass textures. Cozy Nature is free on Fab, but Epic's licence doesn't let anyone share their source files. So this repository holds **Other5 stand-ins** at the same paths:
plain boxes, magenta-and-grey check textures and simple materials. They keep every map and Blueprint working, and
they're obviously placeholders. `StandIns.json` lists each one and where the real asset comes from.

To get the real look, use **Tools > Other5 Setup** in the Other5 Creator. It opens each Fab listing (you add it to your
library with your own Epic account, which is where you accept the licence), imports it, and puts it in place of the
stand-in. Your Creation's paks then ship the real art, cooked, under your own licence. The real files live in your
**Other5 library** (by default a folder `Other5Library` next to your project folder), never in this repository.

Everything else here (maps, actors, Blueprints, the label) is Other5's own.

## Notes
- No other plugins are required. The two game modes use Other5Combat and Other5ThirdPerson.
- Five landscape pieces in `Forest_Partition` point at an old ground-material path (`MS_ForestFloorV1/...`) and show the
  default material. That's a known leftover from before this version.
