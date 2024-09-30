import random

# Function to generate random vital signs
def generate_vital_signs(num_sets=50):
    vital_signs = []
    for _ in range(num_sets):
        # Generate random temperature between 97.0°F and 100.4°F
        temperature = round(random.uniform(97.0, 100.4), 1)
        
        # Generate random SpO2 level between 90% and 100%
        spo2 = random.randint(90, 100)
        
        # Generate random pulse rate between 60 and 100 bpm
        pulse_rate = random.randint(60, 100)
        
        vital_signs.append({
            'Temperature (°F)': temperature,
            'SpO2 (%)': spo2,
            'Pulse Rate (bpm)': pulse_rate
        })
    
    return vital_signs

# Generate 50 sets of vital signs
vital_signs_data = generate_vital_signs()

# Print the generated vital signs data
for index, vitals in enumerate(vital_signs_data, start=1):
    print(f"Set {index}: {vitals}")
