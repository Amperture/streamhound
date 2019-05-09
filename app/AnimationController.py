from bibliopixel.builder import Builder


class AnimationController:

    default_anim_desc = {}

    def __init__(self):
        self.default_anim_desc = {
            'animation': {
                'typename': '$bpa.strip.Twinkle',
                'colors': ('[0, 0, 255], [0, 255, 0]')
            }
        }
        self.controller = Builder(
            desc=self.default_anim_desc,
            threaded=True
        )
        self.controller.start()
        return

    def stop(self):
        self.controller.stop()

    def start(self):
        self.controller.stop()

    def delete(self):
        self.controller.stop()
        del self.controller

    def newAnim(self, animName, animColorList, colorPlural=False):
        desc = {
            'animation': {
                'typename': animName,
                'colors': animColorList,
            }

        }
        self._launchAnim(desc)
        return

    def colorsAppend(self, animColorList):
        if not self.default_anim_desc['animation']['colors']:
            raise Exception(
                "Cannot append colors, singular color is being used!"
            )
        new_colors = (self.default_anim_desc['animation']['colors'] +
                      "," +
                      animColorList)
        self.default_anim_desc['animation']['colors'] = new_colors
        self._launchAnim(self.default_anim_desc)
        return 0

    def _launchAnim(self, desc):
        self.controller.stop()

        if self.controller.is_running:
            raise Exception('Animation Controller Failed to Stop!')

        del self.controller
        self.controller = Builder(
            desc=desc,
            threaded=True
        )
        self.controller.start()
        if not self.controller.is_running:
            raise Exception('New Animation Failed to run!')

        return
