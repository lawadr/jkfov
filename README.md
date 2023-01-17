# Jedi Knight patches

This repository contains patches (in IPS format) for _Jedi Knight: Dark Forces II_ and _Jedi Knight: Mysteries of the Sith_ that were were originally created by [Max Thomas](https://maxthomas.dev/dk2-mots/).

## Field of view

Both games are hardcoded to a 90 degree field of view. These patches increase the field of view to 120.

* `jk-fov120.ips` is for _Jedi Knight: Dark Forces II_
* `jkm-fov120.ips` is for _Jedi Knight: Mysteries of the Sith_

The original version of the patch for _Jedi Knight: Mysteries of the Sith_ causes crashes, black screens and other glitches at certain points in the game, as well as when zooming in and out with the scoped rifle and using force lightning. These happen due to a corruption of the floating point register stack, as it replaces instructions that push a single value to the stack with instructions that push three:

```asm
fld  DWORD PTR ds:0x57c19c
fst  DWORD PTR [esp+0x8]
fild DWORD PTR [esp+0x8]
fld  DWORD PTR ds:0x57ae20
```

This version of the patch simplifies the above to leave only one value on the stack, eliminating the issues:

```asm
fld  DWORD PTR ds:0x57c19c
fstp DWORD PTR [esp+0x8]
fld  DWORD PTR ds:0x57ae20
```

Accompanying these patches is a simple script to generate additional patches for either game for any field of view.

### Patch generation script

To generate a 105 field of view patch for _Jedi Knight: Dark Forces II_:

```
python gen.py jk 105 -o jk-fov105.ips 
```

To generate a 110 field of view patch for _Jedi Knight: Mysteries of the Sith_:

```
python gen.py jkm 110 -o jkm-fov110.ips
```

## Level of detail

Both games have very low distances for switching to lower level of detail models and smaller base mipmap levels. These patches force these distances to 200, effectively ensuring that the highest level of detail models and biggest base mipmap levels are used at all times.

* `jk-mipmapfix.ips` is for _Jedi Knight: Dark Forces II_
* `jkm-mipmapfix.ips` is for _Jedi Knight: Mysteries of the Sith_
