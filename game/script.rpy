# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define s = Character("Sidney")
define j = Character("Jack")
define l = Character("Len")
define y = Character("Yoky")
define sl = Character("Silias")
define sy = Character("Sylvian")
define e = Character("Elizabeth")
define a = Character("Amy")
define ar = Character("Arvad")

#

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    "The Travers have never been all together, {w=1.0}not until one night in the middle of summer."

    s "{i}huff...{/i}"

    "It's almost a troubling thought to Sidney that everything she had ever owned had fit within the surface of their dining table."
    "Yet, {w=0.5}relief is the only thing that watches over at the moment."

    s "{i}It's done. {w=0.2}And now this is where I'll be from now on.{/i}"

    "..."

    "This house was set down between the expanse of the faded brown woods and the dying spark of an old suburbia."
    "Not quite unreachable from the stretch of the the city, and all the more untouched over the years of age old refusal to leave the property behind."
    "A couple years ago the town completed the {i}Old Fern Parklands project{/i} that flowed tangles of uprooted concrete paths in the hopes for a more walkable forest experience."
    "A wonderful way to bring life to a dense landscape unfooted by man."
    "Along the pathways connected three more towns that were long seperated from the mass of trees."
    "No matter how far you stray from the path, {w=0.5}with enough effort and hope, a lost soul can find their way back to society."
    "The first months of the project opening were busy for sure, {w=0.5}but the wonder of it died off slowly once the convenience of cars and public transport took back the patience and dignity of the townsfolk."
    return
