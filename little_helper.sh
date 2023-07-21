echo " A little helper getting started..."
pip install -e .
python raindeer/main.py --mode download-all

if python -m coverage --version > /dev/null 2>&1; then
    echo "'coverage' is installed. Running 'coverage'..."
    # Unset DISPLAY
    coverage run -m unittest discover
    coverage report >> results/results.md
    #rm -r test_data
    rm google.com 
    rm .coverage
else
    echo "'coverage' is not installed. Please install it and try again."
fi
if command -v tokei > /dev/null 2>&1; then
    echo "'tokei' is installed. Running 'tokei'..."
    tokei >> results/results.md
else
    echo "'tokei' is not installed. Please install it and try again."
fi
echo "DONE please look at results/results.md for some project stats"
