# Maze-Builder
Maze builder is a simple python algorithm that solves a maze utilizing recursion. Please see the directions the overview and directions below:

## Overview
<ul>
  <li>Using Python's Tkinter library I have created a maze game which using depth first search (DFS) to arrive at the solution</li>
  <li>The red lines in the document show the current route of the algorithm</li>
  <li>The gray lines show an "undo" where the algorithm has hit a dead end and takes a different route</li>
  <li>The Maze starts in the top left and completes in the bottom right</li>
</ul>

## Directions
<ol>
  <li>Navigate to the Main.py file</li>
  <li>Update the arguments of the Maze constructor in the main() function utilizing the following examples</li>
  <li><code>Maze(<strong>[OffsetX]</strong>,<strong>[OffsetY]</strong>,<strong>[# of Rows]</strong>,<strong>[# of Columns]</strong>,<strong>[Tile/Cell Width]</strong>,<strong>[Tile/Cell Height]</strong>)</code></li>
  <li>Open up terminal and run <code>python Main.py</code></li>
</ol>
<hr/>
<em>- I suggest offsetting both x and y by a minimum of 10 - for some reason on MacOS the maze gets cut off unless you do this</em>
<br/>
<em>- I also suggest using height and width of 50 for the cell/tile's height and width</em>
