import asyncio
from asciimatics.screen import Screen, ManagedScreen
from asciimatics.scene import Scene
from asciimatics.effects import Cycle, Stars
from asciimatics.renderers import FigletText
from asciimatics.widgets import Frame, Layout, Text


fairgame_ascii_art = """
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,..............,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,,,,,,,,..........................,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,,,,........,**/////////**............,,,,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,,.....,*/*.......,/,......,//*..........,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,.....,/*...........,/......,,...,/*.........,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,....,/,.............,/.........,,...//.........,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,....,/,...............,/...........,,..,/*........,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,....,/...........*,,*..,/....,///,....,...,/,.......,,,,,,,,,,,,,,
,,,,,,,,,,,,,....,/...........,,...,.,/..*(*.../(,...,...,/,.......,,,,,,,,,,,,,
,,,,,,,,,,,,,..../,...........,*..*,.,/..,//..,//,....,...,(,.......,,,,,,,,,,,,
,,,,,,,,,,,,,...,/,..................,/....,***........,..../,......,,,,,,,,,,,,
,,,,,,,,,,,,....,/,..................,/.................,...*/......,,,,,,,,,,,,
,,,,,,,,,,,,...../,......*(((//**,,..,/.................,..../*.....,,,,,,,,,,,,
,,,,,,,,,,,,,....,/........*((((((((((/..,..,*.,*........,..../,....,,,,,,,,,,,,
,,,,,,,,,,,,,.....,/,........,*/((((((/..,..,*.,*........,....**...,,,,,,,,,,,,,
,,,,,,,,,,,,,,....../*.............,*///////////*.......,...../*...,,,,,,,,,,,,,
,,,,,,,,,,,,,,,.......//,............,/.............,,.....,//,...,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,.......,/*..........,/......,,,......,,//*.....,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,..........*//,.....,/........,,*///,........,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,.............,**//(////*,,,.............,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,,,,...................................,,,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,,,,,,,,...........................,,,,,,,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,................,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
"""

class DisplayUI:
    def __init__(self):
        self.loop = asyncio.get_event_loop()
        self.screen = Screen.open()
        self.effects = []

        frame = Frame(self.screen, 80, 20, has_border=False)
        layout = Layout([1, 1, 1, 1])
        frame.add_layout(layout)

        end_time = self.loop.time() + 5.0
        self.loop.call_soon(self.update_screen, end_time, self.loop, self.screen)
        self.screen.set_scenes([Scene(frame,500)])
        self.screen.set_title()
    def __del__(self):
        pass

    def update_screen(self, end_time, loop: asyncio.AbstractEventLoop, screen: Screen):
        screen.draw_next_frame()
        if loop.time() < end_time:
            loop.call_later(0.05, self.update_screen, end_time, loop, screen)
        else:
            loop.stop()

    # def init_text(self):
    #     self.effects = [
    #         Cycle(
    #             screen,
    #             FigletText("ASCIIMATICS", font='big'),
    #             screen.height // 2 - 8),
    #         Cycle(
    #             screen,
    #             FigletText("ROCKS!", font='big'),
    #             screen.height // 2 + 3),
    #         Stars(screen, (screen.width + screen.height) // 2)
    #     ]
    #     screen.set_scenes([Scene(effects, 500)])

    def update_text(self,item):
        pass

    def start(self):
        self.loop.run_forever()
        self.loop.close()
        self.screen.close()


stuff = DisplayUI()
stuff.start()


# @ManagedScreen
# def demo(screen):
#     effects = [
#         Cycle(
#             screen,
#             FigletText("ASCIIMATICS", font='big'),
#             screen.height // 2 - 8),
#         Cycle(
#             screen,
#             FigletText("ROCKS!", font='big'),
#             screen.height // 2 + 3),
#         Stars(screen, (screen.width + screen.height) // 2)
#     ]
#     screen.play([Scene(effects, 500)])
#
# demo()