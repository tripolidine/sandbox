define knows_susan = False
define player_name = None

define narrator = Character(None, color="#000000")

define v = Character('Victor', color="#c8ffc8", show_two_window=True)
define character.b = Character('Becky', show_two_window=True)
$ b.fondness = 10

define p = DynamicCharacter("char_name(player_name, 'Me', player_name)", show_two_window=True)
define hr = DynamicCharacter("char_name('Susan', 'Mysterious Lady', knows_susan)", show_two_window=True)

image hr = Placeholder("girl")
image v = Placeholder("boy")
