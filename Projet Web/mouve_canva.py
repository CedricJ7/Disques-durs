from browser import document

class ElementMove:

    def __init__(self, moving):
        """Make "moving" element movable with the mouse"""
        self.moving = moving
        self.is_moving = False
        self.moving.bind("mousedown", self.start)
        self.moving.bind("mouseup", self.stop)
        moving.style.cursor = "move"

    def start(self, event):
        """When user clicks on the moving element, set boolean is_moving
        to True and store mouse and moving element positions"""
        self.is_moving = True
        self.mouse_pos = [event.x, event.y]
        self.elt_pos = [self.moving.left, self.moving.top]
        document.bind("mousemove", self.move)
        # prevent default behaviour to avoid selecting the moving element
        event.preventDefault()

    def move(self, event):
        """User moves the mouse"""
        if not self.is_moving:
            return

        # set new moving element coordinates
        self.moving.left = self.elt_pos[0] + event.x - self.mouse_pos[0]
        self.moving.top = self.elt_pos[1] + event.y - self.mouse_pos[1]

    def stop(self, event):
        """When user releases the mouse button, stop moving the element"""
        self.is_moving = False
        document.unbind("mousemove")

ElementMove(document["moving"])