import csv
from pathlib import Path

try:
    import readline
except ImportError:
    pass

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


DATA_FILE = Path(__file__).with_name("raw_skills.csv")


def load_roles(file_path):
    roles = []
    skill_descriptions = []

    with open(file_path, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            roles.append(row["role"])
            skill_descriptions.append(row["skills"])

    return roles, skill_descriptions


def get_user_skills():
    print("\nWelcome to the Tech Stack Recommender!")
    print("Enter at least 3 technology-related skills, interests, or keywords.\n")

    while True:
        user_input = input("Enter your skills/interests: ").strip().lower()

        skills = user_input.replace(",", " ").split()

        if len(skills) >= 3:
            return skills

        print("Please enter at least 3 skills, for example: Python, Cloud Computing, Automation")


def recommend_roles(user_skills, roles, skill_descriptions, top_n=3):
    user_profile = " ".join(user_skills)

    vectorizer = TfidfVectorizer(stop_words="english")

    role_vectors = vectorizer.fit_transform(skill_descriptions)
    user_vector = vectorizer.transform([user_profile])

    similarity_scores = cosine_similarity(user_vector, role_vectors).flatten()

    recommendations = list(zip(roles, similarity_scores, skill_descriptions))

    recommendations.sort(key=lambda item: item[1], reverse=True)

    return recommendations[:top_n]


def main():
    roles, skill_descriptions = load_roles(DATA_FILE)

    user_skills = get_user_skills()

    recommendations = recommend_roles(user_skills, roles, skill_descriptions)

    print("\nTop 3 Recommended Career Paths:\n")

    for index, (role, match_score, role_skills) in enumerate(recommendations, start=1):
        percentage = match_score * 100
        print(f"{index}. {role}")
        print(f"   Match Score: {percentage:.2f}%")
        print(f"   Related Skills: {role_skills}\n")


if __name__ == "__main__":
    main()