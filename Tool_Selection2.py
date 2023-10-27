import random
import matplotlib.pyplot as plt

# Sample list of criteria with corresponding scores
criteria_scores = {
    "Robustness": 6,
    "Performance": 6,
    "Algorithm": 4,
    "Modular": 7,
    "Real-time": 6,
    "Machine-readable output": 5,
    "Ability to verify C programs":6,
    "Flexibility":4
}

# Sample list of tools with features (for demonstration)
tools = [
    {"name": "UPPAAL", "features": ["Symbolic model checking", "flexible", "Open source", "real-time", "Machine-readable output", "Timed automata", "STL-Compilant", "Cooperative", "Counterexample generation", "Scalable", "Graphical user interface", "GUI", "support for multiple input formats"]},
    {"name": "CPA-Checker", "features": ["Support for a variety of verification techniques", "DLBE", "Scalable", "Open-source", "Support for multiple input formats", "Support for multiple SMT solvers", "Support for counterexample guided abstraction refinement", "counter-example generation", "Flexible", "Modular", "Cooperative"]},
    {"name": "Symbiotic", "features": ["Automatic abstraction refinement", "Support for a variety of properties", "Scalable", "Open source", "Probabilistic verification", "Support for multiple SMT solvers", "Support for counterexample guided abstraction refinement", "GUI", "counter-example generation", "Flexible", "Modular", "Cooperative"]},
    {"name": "CBMC", "features": ["Bounded model checking", "open-source", "Counterexample-guided abstraction refinement", "User-defined assertions", "Memory safety", "Parallelization", "Scalable", "Counter example generation", "cooperative", "Symbolic execution", "model checking", "Modular", "Flexible"]},
    {"name": "ESBMC", "features": ["User-defined assertions", "open-source", "Memory safety", "Parallelization", "Scalable", "User-defined assertions", "Context-bounded model checking", "Machine-readable output", "cooperative"]},
    {"name": "DIVINE", "features": ["Model checking", "flexible", "Symbolic execution", "Abstraction", "Counterexample generation", "Probabilistic verification", "Scalable", "Machine-readable output", "cooperative"]},
    {"name": "ESBMC-INC", "features": ["User-defined assertions", "Context-bounded model checking", "Memory safety", "Parallelization", "Scalable", "cooperative", "Machine-readable output", "counter-example generation"]},
    {"name": "Brick", "features": ["open-source", "scalable", "GUI", "model checking", "counte-examplegenration", "Machine-readable output", "cooperative"]},
    {"name": "Uatomizer", "features": ["Probabilistic model checking", "Machine-readable output", "Abstraction", "Composition", "Counterexample generation", "open-source", "Scalable", ""]},
    {"name": "Pesco", "features": ["Prediction of sequential combinations of verifiers", "Machine-readable output", "Usage of machine learning", "Support for a variety of verifiers", "Scalable", "open-source", ""]},
    {"name": "Utaipan", "features": ["Probabilistic model checking", "Machine-readable output", "Abstraction", "Cooperative", "Counterexample generation", "Scalable", "Graphical user interface", "Documentation", "Support"]},
    {"name": "SPIN", "features": ["Open-source", "Model checking", "Machine-readable output", "model checking", "Simulation", "Embedded C code", "Scalable"]}
]

# Function to calculate the tool score based on criteria and features
def calculate_tool_score(tool, criteria_scores, requirements):
    tool_score = 0
    for criterion, score in criteria_scores.items():
        if criterion in requirements:
            criterion_score = 0
            for keyword in requirements[criterion]:
                keyword = keyword.lower()
                features_str = ' '.join(tool["features"]).lower()
                if keyword in features_str:
                    criterion_score += 1
            tool_score += criterion_score * score
    return tool_score

# Defined requirements (for demonstration)
requirements = {
    "Robustness": ["Support for a variety of properties", "memory safety", "Automatic abstraction refinement"],
    "Performance": ["Scalable", "Counterexample generation", "Support for multiple input formats"],
    "Algorithm": ["Under-approximtion", "Over-approximation", "abstraction", "Large-block-encoding", "Adjustable block-encoding"],
    "Modular": ["Modular", "composition", "DLBE", "share-compliant", "dynamic analysis", "model checking"],
    "Real-time": ["real-time", "STL-compliant", "Symbolic model checking", ""],
    "Machine-readable output": ["XML output", "HTML output"],
    "Ability to verify C programs": ["C-friendly", "cycle-semantic friendly", "Open-source"],
    "Flexibility": ["LTL-compliant", "CTL-compliant", "GUI", "Large-block-encoding", "predicate abstraction"]
}

# Calculate scores for each tool
tool_scores = []
for tool in tools:
    tool_score = calculate_tool_score(tool, criteria_scores, requirements)
    tool_scores.append({"name": tool["name"], "score": tool_score})

# Rank the tools based on their scores
ranked_tools = sorted(tool_scores, key=lambda x: x["score"], reverse=True)

# Display the ranking
print("Tool Ranking:")
for i, tool in enumerate(ranked_tools, 1):
    print(f"{i}. {tool['name']} - Score: {tool['score']}")

# Visualize the results in a bar chart
tools_names = [tool["name"] for tool in ranked_tools]
tools_scores = [tool["score"] for tool in ranked_tools]

plt.bar(tools_names, tools_scores)
plt.xlabel("Tools")
plt.ylabel("Scores")
plt.title("Tool Selection Based on Requirements")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

