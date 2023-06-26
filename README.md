# Disappearing Text App

This repository contains a simple Disappearing Text App implemented using the Tkinter library in Python. The app allows users to enter text in a text box, and if no keystrokes are detected within a defined period of time, the text will be automatically cleared.

## App Features

- The app window is created using the Tkinter library.
- The app title is set as "Disappearing Text App", and the window size is set to 800x500 pixels.
- The app tracks keyboard activity and checks for any keystrokes within a specified time period.
- If no keystrokes are detected within 5 seconds, the text in the input box will be deleted.
- The app provides a label that displays a message indicating whether keyboard activity has been detected or not.

## Usage

To use the Disappearing Text App, run the script and a window will appear. You can type text into the input box. As long as you continue typing or pressing keys within a 5-second interval, the label will display "Keyboard activity detected". If no keys are pressed for 5 seconds, the label will display "No keys were pressed in the last five seconds" and the text in the input box will be cleared.

## Dependencies

The app requires the Tkinter library, which is typically included with Python installations.

