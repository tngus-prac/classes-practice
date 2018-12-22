{
  "cells": [
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {},
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "pygame 1.9.4\n",
            "Hello from the pygame community. https://www.pygame.org/contribute.html\n"
          ]
        }
      ],
      "source": [
        "import pygame\n",
        "pygame.init()\n",
        "\n",
        "win = pygame.display.set_mode((500,500)) # Set make a 500 by 500 surface\n",
        "win.fill((255, 255, 255))                # fill it with white color\n",
        "clock = pygame.time.Clock()              # create clock\n",
        "\n",
        "# Colors are represented in RGB values\n",
        "white = (255,255,255)\n",
        "black = (0,0,0)\n",
        "red = (255,0,0)\n",
        "green = (0,255,0)\n",
        "blue = (0,0,255)\n",
        "\n",
        "# Make a recipe for making button\n",
        "class button():\n",
        "    def __init__(self, color, x,y,width,height, text='Button'):\n",
        "        self.color = color\n",
        "        self.x = x\n",
        "        self.y = y\n",
        "        self.width = width\n",
        "        self.height = height\n",
        "        self.text = text\n",
        "\n",
        "    def draw(self,win):\n",
        "        #Call this method to draw the button on the screen      \n",
        "        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)\n",
        "           \n",
        "        return False\n",
        "\n",
        "def redrawWindow():\n",
        "    win.fill(white)\n",
        "    greenButton.draw(win)\n",
        "\n",
        "# Let's make Buttons!!!\n",
        "greenButton = button(color = green, x = 100,y = 100,width = 100, height=100, text='')\n",
        "\n",
        "# This section runs the game in a loop\n",
        "run = True\n",
        "while run:\n",
        "    # keep loop running at the right speed\n",
        "    clock.tick(27)\n",
        "    # Make sure the game closes when we close the window\n",
        "    for event in pygame.event.get():\n",
        "        pos = pygame.mouse.get_pos()\n",
        "        if event.type == pygame.QUIT:\n",
        "            run = False\n",
        "    \n",
        "    # Make a list of key pressed\n",
        "    keystate = pygame.key.get_pressed()\n",
        "    if keystate[pygame.K_LEFT]:        # if keystate has Left key move left\n",
        "        greenButton.x -=10\n",
        "    if keystate[pygame.K_RIGHT]:       # if keystate has Left key move right\n",
        "        greenButton.x +=10\n",
        "    \n",
        "    # Update the window \n",
        "    redrawWindow()\n",
        "    pygame.display.update()            \n",
        "\n",
        "# When loop ends, QUIT the game\n",
        "pygame.quit()\n",
        "quit()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {},
      "outputs": [],
      "source": []
    }
  ],
  "metadata": {
    "kernelspec": {
      "display_name": "Python 3",
      "language": "python",
      "name": "python3"
    },
    "language_info": {
      "codemirror_mode": {
        "name": "ipython",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.6.5"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 2
}
