# Jedi Knight FoV patches

This repository contains patch files (in IPS format) to change _Jedi Knight: Dark Forces II_ and _Jedi Knight: Mysteries of the Sith_ to 120 field of view (FoV). These patch files were originally created by [Max Thomas](https://maxthomas.dev/dk2-mots/).

Accompanying the two patch files is a simple script to generate additional patch files for either game for any FoV.

## Jedi Knight: Dark Forces II

This patch file is unaltered as it works perfectly.

## Jedi Knight: Mysteries of the Sith

The original patch file causes crashes at certain points in the game, as well as when zooming in and out with the scoped rifle. These crashes happen due to a corruption of the floating point register stack, as it replaces instructions that push a single value to the stack with instructions that push three:

```asm
fld  DWORD PTR ds:0x57c19c
fst  DWORD PTR [esp+0x8]
fild DWORD PTR [esp+0x8]
fld  DWORD PTR ds:0x57ae20
```

This version of the patch file simplifies the above to leave only one value on the stack, eliminating the crashes:

```asm
fld  DWORD PTR ds:0x57c19c
fstp DWORD PTR [esp+0x8]
fld  DWORD PTR ds:0x57ae20
```

## Patch generation script

To generate a 105 FoV patch file for _Jedi Knight: Dark Forces II_:

```
python gen.py -o jk-fov105.ips jk 105
```

To generate a 110 FoV patch file for _Jedi Knight: Mysteries of the Sith_:

```
python gen.py -o jkm-fov110.ips jkm 110
```
