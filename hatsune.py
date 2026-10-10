import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QMovie
from PyQt6.QtWidgets import QApplication, QLabel, QMenu


class DesktopPet(QLabel):
    def __init__(self, gif_path):
        super().__init__()

        # Borderless, always-on-top, and hidden from the taskbar
        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint
            | Qt.WindowType.WindowStaysOnTopHint
            | Qt.WindowType.Tool
        )

        # Transparent background
        self.setAttribute(
            Qt.WidgetAttribute.WA_TranslucentBackground
        )

        # Load animated GIF
        self.movie = QMovie(gif_path)

        if not self.movie.isValid():
            raise FileNotFoundError(
                f"Could not load GIF: {gif_path}"
            )

        self.setMovie(self.movie)
        self.movie.start()

        self.old_pos = None

        # Fit the window to the GIF dimensions
        self.movie.jumpToFrame(0)
        self.adjustSize()

    # Drag the pet with the left mouse button
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.old_pos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        if self.old_pos is not None:
            current_pos = event.globalPosition().toPoint()
            delta = current_pos - self.old_pos

            self.move(self.pos() + delta)
            self.old_pos = current_pos

    def mouseReleaseEvent(self, event):
        self.old_pos = None

    # Right-click menu
    def contextMenuEvent(self, event):
        menu = QMenu(self)
        exit_action = menu.addAction("Bye-bye (Exit Pet)")

        action = menu.exec(event.globalPos())

        if action == exit_action:
            QApplication.quit()

#path : C:\Users\LAM NGUYEN
#put both this code and gif file on path folder

if __name__ == "__main__":
    #dit me ao vl =))))
    # put anime girl on screen ! 
    import os

    app = QApplication(sys.argv)

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    gif_path = os.path.join(BASE_DIR, "hatsune.gif")

    if not os.path.isfile(gif_path):
        print("GIF not found:", gif_path)
        sys.exit(1)

    pet = DesktopPet(gif_path)
    pet.show()

    sys.exit(app.exec())