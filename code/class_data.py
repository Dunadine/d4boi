class_options = {
    1: 'Barbarian',
    2: 'Druid',
    3: 'Necromancer',
    4: 'Rogue',
    5: 'Sorcerer'
}

aspect_names = {
    'Barbarian': {
    1: 'Ancestral Echoes',
    2: 'Ancestral Force',
    3: 'Anemia',
    4: 'Berserk Fury',
    5: 'Berserk Ripping',
    6: 'Bul-Kathos',
    7: 'Burning Rage',
    8: 'Echoing Fury',
    9: 'Encroaching Wrath',
    10: 'Giant Strides',
    11: 'Grasping Whirlwind',
    12: 'Limitless Rage',
    13: 'Numbing Wrath',
    14: 'Perpetual Stomping',
    15: 'Tempering Blows',
    16: 'Dire Whirlwind',
    17: 'Iron Warrior',
    18: 'Relentless Armsmaster',
    19: 'Unrelenting Fury',
    20: 'Battle-Mad',
    21: "Bear Clan Berserker's",
    22: "Bold Chieftain's",
    23: "Brawler's",
    24: 'Death Wish',
    25: 'Devilish',
    26: "Dust Devil's",
    27: 'Earthquake',
    28: "Earthstriker's",
    29: 'Iron Blood',
    30: 'Luckbringer',
    31: "Relentless Berserker's",
    32: "Skullbreaker's",
    33: 'Slaking',
    34: "Steadfast Berserker's",
    35: "Veteran Brawler's",
    36: "Weapon Master's",
    37: 'Windlasher'
    },
    'Druid': {
        1: 'Alpha',
        2: 'Balanced',
        3: 'Ballistic',
        4: 'Blurred Beast',
        5: 'Calm Breeze',
        6: "Changeling's Debt",
        7: 'Crashstone',
        8: 'Cyclonic Force',
        9: 'Dark Howl',
        10: 'Dire Wolf',
        11: 'Earthguard',
        12: 'Lightning Dancer',
        13: 'Mangled',
        14: 'Mending Stone',
        15: 'Mighty Storm',
        16: 'Metamorphic Stone',
        17: 'Nighthowler',
        18: 'Natural Balance',
        19: "Nature's Savagery",
        20: 'Overcharged',
        21: 'Quicksand',
        22: 'Rampaging Werebeast',
        23: 'Retaliation',
        24: "Runeworker's Conduit",
        25: 'Seismic-shift',
        26: 'Shepherd',
        27: 'Shockwave',
        28: 'Skinwalker',
        29: 'Stampede',
        30: 'Stormchaser',
        31: 'Stormclaw',
        32: 'Stormshifter',
        33: 'Symbiotic',
        34: 'Tempest',
        35: 'Trampled Earth',
        36: 'Trickshot',
        37: 'Ursine Horror',
        38: 'Wildrage'
    },
    'Necromancer': {
        1: 'Blighted',
        2: 'Blood Getter',
        3: 'Blood Seeker',
        4: 'Blood-bathed',
        5: 'Blood-soaked',
        6: 'Bursting Bones',
        7: 'Cadaverous',
        8: 'Coldbringer',
        9: 'Decay',
        10: 'Empowering Reaper',
        11: 'Explosive Mist',
        12: 'Exposed Flesh',
        13: 'Fastblood',
        14: 'Flesh-Rending',
        15: 'Frenzied Dead',
        16: 'Grasping Veins',
        17: 'Hardened Bones',
        18: 'Hungry Blood',
        19: 'Hulking',
        20: 'Osseous Gale',
        21: 'Plunging Darkness',
        22: 'Potent Blood',
        23: "Rathma's Chosen",
        24: 'Reanimation',
        25: 'Requiem',
        26: 'Rotting',
        27: 'Sacrificial',
        28: 'Serration',
        29: 'Shielding Storm',
        30: 'Swelling Curse',
        31: 'Tidal',
        32: 'Torturous',
        33: 'Torment',
        34: 'Ultimate Shadow',
        35: 'Unyielding Commander',
        36: 'Untimely Death',
        37: 'Viscous'
    },
    'Rogue': {
        1: 'Arrow Storms',
        2: 'Bladedancer',
        3: 'Blast-Trapper',
        4: 'Branching Volleys',
        5: 'Bursting Venoms',
        6: 'Cheat',
        7: 'Corruption',
        8: 'Cruel Sustenance',
        9: 'Elusive Menace',
        10: 'Encircling Blades',
        11: 'Enshrouding',
        12: 'Escape Artist',
        13: 'Explosive Verve',
        14: 'Frostbitten',
        15: 'Icy Alchemist',
        16: 'Imitated Imbuement',
        17: 'Infiltrator',
        18: 'Lethal Dusk',
        19: 'Noxious Ice',
        20: 'Opportunist',
        21: 'Quickening Fog',
        22: 'Ravager',
        23: 'Ravenous',
        24: 'Repeating',
        25: 'Shadowslicer',
        26: 'Snap Frozen',
        27: 'Siphoned Victuals',
        28: 'Stolen Vigor',
        29: 'Surprise',
        30: 'Synergy',
        31: 'Toxic Alchemist',
        32: 'Trickshot',
        33: 'Trickster',
        34: 'Umbrous',
        35: 'Uncanny Treachery',
        36: 'Unstable Imbuements',
        37: 'Vengeful'
    },
    'Sorcerer': {
        1: 'Blistering Storm',
        2: 'Burning Pyre',
        3: 'Convection',
        4: 'Cryomancer',
        5: 'Cursed Flames',
        6: 'Embercore',
        7: 'Empowered Spells',
        8: 'Enchanted Runes',
        9: 'Explosive Ignition',
        10: 'Fireball Barrage',
        11: 'Flame Torrent',
        12: 'Frost Nova',
        13: 'Frostbite',
        14: 'Inferno',
        15: 'Living Lightning',
        16: 'Malevolence',
        17: 'Overload',
        18: 'Pyromania',
        19: 'Raging Inferno',
        20: 'Shocking Power',
        21: 'Snowstorm',
        22: 'Storm Weaver',
        23: 'Tempest Fury',
        24: 'Thunderstorm',
        25: 'Volcanic Eruption',
        26: 'Warped Time',
        27: 'Whirling Dervish',
        28: 'Whispering Shadows'
    },
    'General': {
    1: 'Accelerating',
    2: 'Disobedience',
    3: 'Inner Calm',
    4: 'Might',
    5: 'Retribution',
    6: 'Shared Misery',
    7: 'Crowded Sage',
    8: 'Deflecting Barrier',
    9: 'Expectant',
    10: 'Protector',
    11: 'Umbral',
    12: 'Assimilation',
    13: 'Conceited',
    14: "Edgemaster's",
    15: 'Eluding',
    16: "Exploiter's",
    17: 'Ghostwalker',
    18: 'Needleflare',
    19: 'Protecting',
    20: 'Rapid',
    21: 'Smiting',
    22: 'Starlight',
    23: 'Wind Striker'
    }
}
