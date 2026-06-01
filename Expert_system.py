# Rule-Based Expert System using Forward Chaining

# Rule Base (If-Then Rules)
rules = {
    ("fever", "cough"): "flu",
    ("fever", "headache"): "viral infection",
    ("flu", "body pain"): "severe flu",
    ("cough", "sore throat"): "cold",
    ("cold", "fever"): "infection"
}

# Take user symptoms input
user_input = input("Enter symptoms separated by comma: ").lower()

# Convert input into facts list
facts = [symptom.strip() for symptom in user_input.split(",")]

print("\nUser Symptoms:", facts)

# Store reasoning steps
inference_steps = []

# Forward chaining
new_fact_added = True

while new_fact_added:
    new_fact_added = False

    for condition, conclusion in rules.items():

        # Check all conditions
        if all(symptom in facts for symptom in condition):

            # Add new conclusion
            if conclusion not in facts:
                facts.append(conclusion)

                step = f"Rule Applied: {condition} -> {conclusion}"
                inference_steps.append(step)

                new_fact_added = True

# Display inference steps
print("\nInference Steps:")

if inference_steps:
    for step in inference_steps:
        print(step)
else:
    print("No matching rules found.")

# Final conclusion
print("\nFinal Conclusion:")
print(facts)
