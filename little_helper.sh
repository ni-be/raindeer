echo " A little helper for getting started..."
pip install -e .
raindeer --mode download-all

if python -m coverage --version > /dev/null 2>&1; then
    echo "'coverage' is installed. Running 'coverage'..."
    # Unset DISPLAY
    coverage run -m unittest discover
    echo "Coverage Results" >> results/results.md
    coverage report >> results/results.md
    #rm -r test_data
    rm google.com 
    rm .coverage
else
    if python -m unittest --version > /dev/null 2>&1; then
        echo "Unittest is installed. Running Unittest Instead..."
        python -m unittest
    else
        echo "Neither Unittest nor"
        echo "'coverage' is not installed. Please install it and try again."
    fi
fi
if command -v tokei > /dev/null 2>&1; then
    echo "'tokei' is installed. Running 'tokei'..."
    echo "Tokei results" >> results/results.md
    tokei >> results/results.md
    
else
    echo "'tokei' is not installed. Please install it to gets the stats / NOT NECESSARY / CAN BE IGNORED"
    echo " you can run tokei mannualy by running '$ tokei ' in the project root"
fi
echo "DONE please look at results/results.md for some project stats"
