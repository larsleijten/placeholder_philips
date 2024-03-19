import sys
import random
import SimpleITK as sitk
import json
from typing import Union
from pathlib import Path


def load_mha(file_path):
    try:
        img = sitk.ReadImage(file_path)
        return True
    except Exception as e:
        print(f"Error loading mha file: {e}")
        return False


def generate_risk_score():
    return random.random()


def main(ct_file="ct.mha", pt_file="pet.mha", coord_file="coord.json"):
    images = Path("/images/")
    ct_path = images / ct_file
    pt_path = images / pt_file
    coord_path = images / coord_file

    # Load coordinates
    with open(coord_path, "r") as f:
        data = json.load(f)
    coord = (data["x"], data["y"], data["z"])

    # Load images and generate risk score
    if load_mha(ct_path) and load_mha(pt_path):
        risk_score = generate_risk_score()

    print(f"Risk score: {risk_score}")


if __name__ == "__main__":
    if len(sys.argv) == 1:
        main()
    elif len(sys.argv) == 4:
        ct_file = sys.argv[1]
        pt_file = sys.argv[2]
        coord_file = sys.argv[3]
        main(ct_file, pt_file, coord_file)
    else:
        print("Invalid number of arguments")
        sys.exit(1)
