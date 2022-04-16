#!/usr/bin/env python3
"""Calculate BMR and TDEE"""

import argparse


# define and parse args
parser = argparse.ArgumentParser(
    description="Calculate BMR and track calories.")
parser.add_argument(
    "-he", "--height", type=float, required=True, help='Height (feet.inches)')
parser.add_argument(
    "-w", "--weight", type=float, required=True, help='Weight (lb)')
parser.add_argument(
    "-y", "--age", type=int, required=True, help='Age (years)')
parser.add_argument(
    "-s", "--sex", type=str, required=True, help='Sex (m/f)')
parser.add_argument(
    "-a", "--activity", type=str, required=False, help='Activity level (range 1 ~ 5, sedentary to very active)')
parser.add_argument(
    "-n", "--name", type=str, required=False, help='Name (optional)')

args = parser.parse_args()

activity = {
    '1': ["sedentary (little or no exercise)", 1.2],
    '2': ["light activity (light exercise/sports 1 to 3 days per week)", 1.375],
    '3': ["moderate activity (moderate exercise/sports 3 to 5 days per week)", 1.55],
    '4': ["very active (hard exercise/sports 6 to 7 days per week)", 1.725],
    '5': ["extra active (very hard exercise/sports 6 to 7 days per week and physical job)", 1.9]
}


def to_metric(h, w):
    """Convert imperial height/weight to metric"""
    h = (((h//1)*12+((h % 1)*10))*2.54)
    w = w*0.45359237
    return h, w


def harris_benedict(w, h, s, a):
    """Calculate BMR using Harris-Benedict equation"""
    bmr = ((w*10) + (6.25*h) + (5*a))
    if s == 'm':
        bmr += 5
    else:
        bmr -= 161
    return bmr


def katch_mcardle(bmr):
    """Calculate TDEE from BMR and activity multiplier"""
    if args.activity:
        multiplier = args.activity
    else:
        print("\nAverage Daily Activity Level:\n")
        for k in activity:
            print(k, ": ", activity[k][0])
        print("\n")
        multiplier = input(
            "Please enter the option that most closely resembles your average activity level (1-5): ")
    tdee = bmr*activity[multiplier][1]
    return tdee


if __name__ == '__main__':
    a, s = args.age, args.sex
    h, w = to_metric(args.height, args.weight)
    print("Calculating basal metabolic rate (BMR)...")
    bmr = harris_benedict(w, h, s, a)
    print("Calculating total daily energy expenditure (TDEE)...")
    tdee = katch_mcardle(bmr)
    print(
        f"\nYour BMR is ~{int(bmr)} calories.\nYour TDEE is ~{int(tdee)} calories.\n")