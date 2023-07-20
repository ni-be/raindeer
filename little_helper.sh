#!/bin/bash
   # Step 2: Run coverage command
   coverage run -m unittest discover

   # Step 3: Run coverage report
   coverage report >> results/results.md

   # Step 4: Run tokei command
   tokei >> results/results.md
  
