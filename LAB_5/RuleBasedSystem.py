class RuleBasedSystem:
    def __init__(self):
        self.rules = []
        self.facts = set()

    def add_rule(self, condition_func, action_func, description):
        """Adds a rule to the Knowledge Base."""
        self.rules.append({
            "condition": condition_func,
            "action": action_func,
            "desc": description
        })

    def add_fact(self, fact):
        """Adds a fact to Working Memory."""
        self.facts.add(fact)

    def run(self):
        """Inference Engine using Forward Chaining."""
        fired_rules = set()
        inferred_new_facts = True

        print("--- Starting Inference Engine ---")
        while inferred_new_facts:
            inferred_new_facts = False
            for i, rule in enumerate(self.rules):
                if i not in fired_rules:
                    # Check if conditions are met by current facts
                    if rule["condition"](self.facts):
                        print(f"[FIRE] Rule triggered: {rule['desc']}")
                        new_fact = rule["action"]()
                        if new_fact and new_fact not in self.facts:
                            self.facts.add(new_fact)
                            inferred_new_facts = True
                        fired_rules.add(i)
        print("--- Inference Complete ---")

# --- Example Usage: Medical Diagnostic Assistant ---
system = RuleBasedSystem()

# Define Rules
# Rule 1: IF fever AND cough THEN possible_flu = true
system.add_rule(
    condition_func=lambda facts: "fever" in facts and "cough" in facts,
    action_func=lambda: "possible_flu",
    description="If fever and cough are present, suspect flu."
)

# Rule 2: IF possible_flu AND body_aches THEN recommend_prescription = rest_and_hydration
system.add_rule(
    condition_func=lambda facts: "possible_flu" in facts and "body_aches" in facts,
    action_func=lambda: "recommend_rest",
    description="If possible flu and body aches, recommend medical rest."
)

# Add initial facts to Working Memory
system.add_fact("fever")
system.add_fact("cough")
system.add_fact("body_aches")

# Run the engine
system.run()
print("Final Working Memory Facts:", system.facts)