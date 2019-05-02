from bibliopixel.builder import Builder


class AnimationController:

    def __init__(self):
        self.controller = Builder(
            desc={},
            threaded=True
        )
        self.controller.desc.animation['typename'] = '$bpa.strip.Twinkle'
        self.controller.desc.animation['colors'] = ('[255, 127, 127], '
                                                    '[0, 255, 0]')
        self.controller.start()
        return

    def stop(self):
        self.controller.stop()

    def start(self):
        self.controller.stop()

    def delete(self):
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
