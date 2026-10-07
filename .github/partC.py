import pandas as pd
import subprocess
import os

# ============================================================
# PART C: MULTI-PARADIGM PROGRAMMING (PYTHON)
# Integrated Learner Dashboard
# ============================================================

BASE_FOLDER = os.path.dirname(os.path.abspath(__file__))
HASKELL_FILE = os.path.join(BASE_FOLDER, "partA.hs")
PROLOG_FILE = os.path.join(BASE_FOLDER, "partB.pl")


# ============================================================
# OBJECT-ORIENTED PROGRAMMING
# ============================================================

class Learner:
    def __init__(self, learner_id, name, completed_modules, scores):
        # Input validation
        if not learner_id.strip():
            raise ValueError("Learner ID cannot be empty.")

        if not name.strip():
            raise ValueError("Learner name cannot be empty.")

        if not scores:
            raise ValueError("Scores cannot be empty.")

        for score in scores:
            if not isinstance(score, (int, float)):
                raise ValueError("Scores must be numeric.")
            if score < 0 or score > 100:
                raise ValueError("Score must be between 0 and 100.")

        self.learner_id = learner_id
        self.name = name
        self.completed_modules = completed_modules
        self.scores = scores

    def calculate_average(self):
        return sum(self.scores) / len(self.scores)

    def predict_performance(self):
        average = self.calculate_average()

        if average >= 80:
            return "Excellent"
        elif average >= 60:
            return "Good"
        elif average >= 50:
            return "Average"
        else:
            return "Needs Improvement"


# ============================================================
# CONSISTENT LEARNER DATA
# Scores follow Part A Haskell.
# Completed modules for AM001-AM006 follow Part B Prolog.
# AM007 and AM008 are in Part A but not in the current Part B.
# ============================================================

learners = [
    Learner("AM001", "Hana",   ["C101", "C102", "C103"], [75, 60, 70]),
    Learner("AM002", "Achik",  ["C101", "C102"], [85, 90, 90]),
    Learner("AM003", "Aina",   ["C101", "C102", "C103", "C104", "C105", "C106"], [60, 75, 70]),
    Learner("AM004", "Amin",   ["C101"], [60, 65, 70]),
    Learner("AM005", "Zafran", ["C101", "C102", "C103"], [90, 95, 90]),
    Learner("AM006", "Adam",   ["C101", "C102"], [85, 90, 80]),
    Learner("AM007", "Farah",  [], [80, 80, 80]),
    Learner("AM008", "Sara",   [], [90, 95, 90])
]


# ============================================================
# FUNCTIONAL-STYLE OPERATIONS
# ============================================================

# 1. map() + lambda: calculate average for every learner.
averages = list(
    map(lambda learner: learner.calculate_average(), learners)
)

# 2. filter() + lambda: select learners with average >= 80.
high_achievers = list(
    filter(lambda learner: learner.calculate_average() >= 80, learners)
)

# 3. List comprehension: transform learner objects into names.
learner_names = [learner.name for learner in learners]


# PART A: HASKELL INTEGRATION


def run_part_a():
    print("\n============================================")
    print("       PART A - PERFORMANCE ANALYSIS")
    print("============================================")

    if not os.path.exists(HASKELL_FILE):
        print("\nERROR: partA.hs was not found.")
        return

    try:
        result = subprocess.run(
            ["runghc", HASKELL_FILE],
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            print("\n" + result.stdout)
        else:
            print("\nHaskell Error:")
            print(result.stderr)

    except FileNotFoundError:
        print("\nERROR: runghc was not found.")
        print("Install GHC and make sure runghc is available in PATH.")


# PART B: PROLOG INTEGRATION

def run_prolog_query(query):
    if not os.path.exists(PROLOG_FILE):
        return None, "partB.pl was not found."

    try:
        result = subprocess.run(
            [
                "swipl",
                "-q",
                "-s",
                PROLOG_FILE,
                "-g",
                query,
                "-t",
                "halt"
            ],
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            return result.stdout.strip(), None

        return None, result.stderr.strip()

    except FileNotFoundError:
        return None, "SWI-Prolog was not found. Make sure swipl is available in PATH."


def run_part_b():
    print("\n============================================")
    print("          PART B - MODULE ADVISORY")
    print("============================================")

    output, error = run_prolog_query(
        "writeln('Prolog knowledge base loaded successfully')"
    )

    if error:
        print("\nProlog Error:", error)
        return

    print("\n" + output)
    print("\nAvailable advisory functions:")
    print("- Completed modules")
    print("- Module eligibility")
    print("- Recommended modules")
    print("- Certification eligibility")


# ============================================================
# LEARNER DASHBOARD FUNCTIONS
# ============================================================

def display_learners():
    print("\n============================================")
    print("              LEARNER DETAILS")
    print("============================================")

    for learner in learners:
        completed = (
            ", ".join(learner.completed_modules)
            if learner.completed_modules
            else "N/A in Part B"
        )

        print(f"\nLearner ID       : {learner.learner_id}")
        print(f"Name             : {learner.name}")
        print(f"Completed Modules: {completed}")
        print(f"Scores           : {learner.scores}")
        print(f"Average          : {learner.calculate_average():.2f}")
        print(f"Performance      : {learner.predict_performance()}")


def performance_analysis():
    print("\n============================================")
    print("           PERFORMANCE ANALYSIS")
    print("============================================")

    for learner in learners:
        print(
            f"{learner.learner_id} | {learner.name} | "
            f"Average: {learner.calculate_average():.2f} | "
            f"{learner.predict_performance()}"
        )


def display_high_achievers():
    print("\n============================================")
    print("          HIGH-ACHIEVING LEARNERS")
    print("============================================")
    print("\nLearners with average >= 80:\n")

    for learner in high_achievers:
        print(
            f"{learner.learner_id} | {learner.name} | "
            f"Average: {learner.calculate_average():.2f}"
        )


def display_top_performer():
    print("\n============================================")
    print("              TOP PERFORMER")
    print("============================================")

    top_learner = learners[0]

    # Same tie rule as Part A:
    # when averages are equal, the later learner is selected.
    for learner in learners[1:]:
        if learner.calculate_average() >= top_learner.calculate_average():
            top_learner = learner

    print(f"Learner ID : {top_learner.learner_id}")
    print(f"Name       : {top_learner.name}")
    print(f"Average    : {top_learner.calculate_average():.2f}")
    print(f"Performance: {top_learner.predict_performance()}")
    print("Tie Rule   : Later learner is selected when averages are equal.")


def integrated_learner_profile():
    print("\n============================================")
    print("       INTEGRATED LEARNER PROFILE")
    print("============================================")

    learner_id = input("Enter Learner ID (example AM001): ").upper().strip()

    selected = next(
        (learner for learner in learners if learner.learner_id == learner_id),
        None
    )

    if selected is None:
        print("\nLearner not found.")
        return

    print("\n--- PERFORMANCE PROFILE ---")
    print(f"Learner ID  : {selected.learner_id}")
    print(f"Name        : {selected.name}")
    print(f"Scores      : {selected.scores}")
    print(f"Average     : {selected.calculate_average():.2f}")
    print(f"Performance : {selected.predict_performance()}")

    # AM007 and AM008 are present in Part A but not in current Part B.
    if learner_id in ("AM007", "AM008"):
        print("\n--- PART B: MODULE ADVISORY ---")
        print(
            f"{learner_id} is available in Part A but is not "
            "defined in the current Part B knowledge base."
        )
        return

    prolog_id = learner_id.lower()

    completed_query = (
        f"findall(C,enrolled({prolog_id},C),L),writeln(L)"
    )
    completed_output, error = run_prolog_query(completed_query)

    print("\n--- PART B: MODULE ADVISORY ---")

    if error:
        print("Prolog Error:", error)
        return

    print("Completed Modules  :", completed_output)

    recommendation_query = (
        f"findall(C,recommend_course({prolog_id},C),L),writeln(L)"
    )
    recommendation_output, error = run_prolog_query(recommendation_query)

    if error:
        print("Recommendation Error:", error)
    else:
        print("Recommended Modules:", recommendation_output)

    certification_query = (
        f"(certification_eligible({prolog_id}) -> "
        "writeln('Eligible for Certification'); "
        "writeln('Not Eligible for Certification'))"
    )
    certification_output, error = run_prolog_query(certification_query)

    if error:
        print("Certification Error:", error)
    else:
        print("Certification      :", certification_output)


def check_module_eligibility():
    print("\n============================================")
    print("         MODULE ELIGIBILITY CHECK")
    print("============================================")

    learner_id = input("Enter Learner ID (AM001-AM006): ").lower().strip()
    course_code = input("Enter Module Code (C101-C106): ").lower().strip()

    valid_ids = ["am001", "am002", "am003", "am004", "am005", "am006"]
    valid_courses = ["c101", "c102", "c103", "c104", "c105", "c106"]

    if learner_id not in valid_ids:
        print("\nLearner ID is not available in Part B.")
        return

    if course_code not in valid_courses:
        print("\nInvalid module code.")
        return

    query = (
        f"(eligible({learner_id},{course_code}) -> "
        "writeln('ELIGIBLE'); writeln('NOT ELIGIBLE'))"
    )

    output, error = run_prolog_query(query)

    if error:
        print("\nProlog Error:", error)
    else:
        print("\nResult:", output)


def pandas_summary():
    print("\n============================================")
    print("         LEARNER SUMMARY AND RANKING")
    print("============================================\n")

    # Functional-style list comprehension used to build table data.
    data = [
        {
            "Learner ID": learner.learner_id,
            "Name": learner.name,
            "Completed Modules": (
                ", ".join(learner.completed_modules)
                if learner.completed_modules
                else "N/A in Part B"
            ),
            "Average": round(learner.calculate_average(), 2),
            "Performance": learner.predict_performance()
        }
        for learner in learners
    ]

    df = pd.DataFrame(data)

    # Rank learners by average score.
    df["Rank"] = (
        df["Average"]
        .rank(method="min", ascending=False)
        .astype(int)
    )

    df = df.sort_values(
        by=["Average", "Learner ID"],
        ascending=[False, True]
    )

    print(df.to_string(index=False))


# ============================================================
# TEST CASES
# Kept in source code as assignment evidence.
# They are intentionally not displayed as dashboard menu items.
# ============================================================

def test_normal_input():
    test = Learner(
        "TEST01",
        "Normal Learner",
        ["C101", "C102", "C103"],
        [85, 90, 90]
    )

    actual_average = round(test.calculate_average(), 2)
    actual_performance = test.predict_performance()

    return (
        actual_average == 88.33
        and actual_performance == "Excellent"
    )


def test_boundary_input():
    test = Learner(
        "TEST02",
        "Boundary Learner",
        ["C101", "C102", "C103"],
        [80, 80, 80]
    )

    return (
        test.calculate_average() == 80
        and test.predict_performance() == "Excellent"
    )


def test_invalid_input():
    try:
        Learner(
            "TEST03",
            "Invalid Learner",
            ["C101"],
            [120]
        )
        return False

    except ValueError:
        return True


def test_tie_case():
    zafran = Learner(
        "AM005",
        "Zafran",
        ["C101", "C102", "C103"],
        [90, 95, 90]
    )

    sara = Learner(
        "AM008",
        "Sara",
        [],
        [90, 95, 90]
    )

    test_learners = [zafran, sara]
    top = test_learners[0]

    for learner in test_learners[1:]:
        if learner.calculate_average() >= top.calculate_average():
            top = learner

    return top.name == "Sara"


# ============================================================
# MAIN DASHBOARD
# ============================================================

def dashboard():
    while True:
        print()
        print("====================================================")
        print("   SMART LEARNING PATHWAY AND CERTIFICATION SYSTEM")
        print("              INTEGRATED LEARNER DASHBOARD")
        print("====================================================")
        print("1. Part A - Performance Analysis")
        print("2. Part B - Module Advisory")
        print("3. View All Learners")
        print("4. Performance Analysis")
        print("5. High-Achieving Learners")
        print("6. Top Performer")
        print("7. Integrated Learner Profile")
        print("8. Check Module Eligibility")
        print("9. Learner Summary and Ranking")
        print("0. Exit")
        print("====================================================")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            run_part_a()
        elif choice == "2":
            run_part_b()
        elif choice == "3":
            display_learners()
        elif choice == "4":
            performance_analysis()
        elif choice == "5":
            display_high_achievers()
        elif choice == "6":
            display_top_performer()
        elif choice == "7":
            integrated_learner_profile()
        elif choice == "8":
            check_module_eligibility()
        elif choice == "9":
            pandas_summary()
        elif choice == "0":
            print("\nThank you. Program ended.")
            break
        else:
            print("\nInvalid choice. Please enter a number from 0 to 9.")


if __name__ == "__main__":
    dashboard()
