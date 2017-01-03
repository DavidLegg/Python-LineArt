LineArt - Python Automatic Drawing
==================================

This is a small project to explore the ability for simple scripts to create abstract art by drawing curves that are constrained and randomized in different ways.

Usage
-----

Use the quick method from main.py, passing a standard drawing name: `'blueshift'`, `'redshift'`, `'bluetaper'`, or `'redtaper'`. Left clicks on the resulting window create previews of the drawing, and right clicks save the drawing. Note: the drawing will save in much higher resolution than the preview. This is especially noticeable for line weights less than 1.

You can also pass settings to the quick method to tweak the appearance of this drawing.

To combine drawing classes, create your own class that inherits from each desired type of Drawing (e.g., `ShiftCombo`, in main.py). Passing arguments to parameters will still work.

A deeper dive is given in 'Interface.md'.

Motivation
----------

I rather enjoy abstract art as backgrounds for my desktop, email, etc. After examining some of my favorite backgrounds, I couldn't help wondering how I might be able to riff on the patterns I saw there: brightly colored, near-parallel curves on a dark background.