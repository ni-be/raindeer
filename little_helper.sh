python raindeer/main.py --mode download-all
coverage run -m unittest discover
coverage report >> results/results.md
tokei report >> results/results.md
rm -r test_data
rm google.com 

print("DONE please look at results/results.md for some project stats") 