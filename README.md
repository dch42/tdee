# tdee
Quick CLI script to calculate TDEE and BMR.

## Setup 🔧
clone the repo and change to directory:
~~~
git clone https://github.com/dch42/tdee.git && cd tdee
~~~

Add executible permissions:
~~~
chmod +x ./tdee.py
~~~

## Usage

Invoke like so:

~~~
tdee.py [-h] [-he HEIGHT] [-w WEIGHT] [-y AGE] [-s SEX] [-a ACTIVITY] [-l LOSE]
~~~

### Options
- `-h, --help`
    - show this help message and exit
- `-he, --height`
    - Height (feet.inches)
- `-w, --weight`
    - Weight (lbs) 
- `-y, --age`
    - Age (years)
- `-s, --sex`
    - Sex (m/f)
- `-a, --activity`
    - Average activity level (range 1~5, sedentary to very active)
- `-l, --lose`
    - Desired number of pounds to lose per week
