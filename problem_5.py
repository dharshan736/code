def find_strongest_trainees():
    trainees = 4  
    rounds = 3
    strength_levels = []  

    for i in range(trainees):
        trainee_strength = []
        for j in range(rounds):
            strength = int(input(f"Enter strength for Trainee {i+1}, Round {j+1}: "))
            if strength < 1 or strength > 200:
                print("INVALID INPUT")
                return
            trainee_strength.append(strength)
        strength_levels.append(trainee_strength)
    
    average_strengths = [round(sum(levels) / rounds) for levels in strength_levels]
    
    max_average = max(average_strengths)
    
    if max_average < 100:
        print("All trainees are unfit")
        return

    print("Trainee Number:")
    for i, avg in enumerate(average_strengths):
        if avg == max_average:
            print(i + 1)

# Run the function
find_strongest_trainees()
