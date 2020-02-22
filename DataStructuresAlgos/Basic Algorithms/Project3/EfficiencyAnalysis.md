# Project 3 Algorithm Efficiency Analysis

## Problem 1: Finding the square root of an integer

My approach here was to get a list of numbers up to the input number - which becomes my time and space limiting factor *n*.  Then I would iterate over this list squaring each number i and comparing it to the input number, which we will call *x*.  If *x* is greater than the squared number then we set current floored square root equal to i.  Once *i^2 > x* then we return the current floored square root.  Given that we are squaring each number and are comparing / capped at the *x* this will have the eff