import numpy as np
import cv2


class Canvas:
    def __init__(self):
        self.canvas = np.zeros((480, 640, 3), dtype=np.uint8)
        self.prev_x, self.prev_y = 0, 0
        self.color = (255, 0, 255)  # Pink default
        self.undo_stack = []
        self.redo_stack = []

    def save_state(self):
        self.undo_stack.append(self.canvas.copy())
        self.redo_stack.clear()

    def draw(self, x, y):
        if self.prev_x == 0:
            self.prev_x, self.prev_y = x, y
            self.save_state()

        cv2.line(
            self.canvas,
            (self.prev_x, self.prev_y),
            (x, y),
            self.color,
            6
        )
        self.prev_x, self.prev_y = x, y

    def undo(self):
        if self.undo_stack:
            self.redo_stack.append(self.canvas.copy())
            self.canvas = self.undo_stack.pop()

    def redo(self):
        if self.redo_stack:
            self.undo_stack.append(self.canvas.copy())
            self.canvas = self.redo_stack.pop()

    def clear(self):
        self.save_state()
        self.canvas[:] = 0
