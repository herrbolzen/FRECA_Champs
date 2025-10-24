import csv

# Add 2025 to Super Licence system

with open("data.csv") as file:
    reader = csv.reader(file)
    next(reader)

# VARIABLES
    elo_br : int # Elo before round()
    elo : int # Elo after round()
    pole_mult : int = 3 # Pole Multiplicator = 3
    pod_mult : int = 5 # Podium Multiplicator = 5
    win_mult : int = 10 # Win Multiplicator = 10
    pole_sc : int # Final Pole Elo Score
    pod_sc: int # Final Podium Elo Score
    win_sc: int # Final Win Elo Score
    driver_elo : dict = {} # List to store elo data for each driver
    season_mult : float
    element : int # Used in for loop later
    count : int = 1 # Used in for loop later

    for row in reader: # Assign variables with their values
        driver = (row[1])
        win_amnt = float(row[2])
        pod_amnt = float(row[3])
        pole_amnt = float(row[4])
        race_amnt = float(row[5])
        sof = float(row[6])
        season = int(row[7])

        # Calculate multiplicator for winning in season X of a single seater career
        if (season == 3):
            season_mult = 1.0
        elif (season == 4):
            season_mult = 0.8
        elif (season == 5):
            season_mult = 0.6

        # Final scores
        pole_sc = (pole_amnt * pole_mult)*season_mult
        pod_sc = (pod_amnt * pod_mult)*season_mult
        win_sc = (win_amnt * win_mult)*season_mult

        # Calculate Elo before rounding, then round it
        elo_br = float((win_sc + pod_sc + pole_sc)/race_amnt)*sof
        elo = round(elo_br, 2)

        # Add new drivers to dictionary
        if driver is not driver_elo:
            driver_elo[driver] = []
        driver_elo[driver] = elo

    # Sort dictionary
    sorted_elo = sorted(driver_elo.items(), key=lambda item: item[1], reverse = True)

    # Print results
    print()
    print("Ranked by Elo")
    print("Pos.", "Name", " ", " "," ", " "," ", "|", "Elo")
    for element in sorted_elo:
        print(count, ".", element[0], "|", element[1])
        count += 1
    print()

