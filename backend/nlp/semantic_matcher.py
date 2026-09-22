from sentence_transformers import SentenceTransformer, util


class SemanticSkillMatcher:

    def __init__(self):
        # Pre-trained semantic NLP model
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    # --------------------------------------------------
    # CALCULATE SEMANTIC SIMILARITY
    # --------------------------------------------------

    def similarity(self, skill1, skill2):

        embeddings = self.model.encode(
            [skill1, skill2],
            convert_to_tensor=True
        )

        score = util.cos_sim(
            embeddings[0],
            embeddings[1]
        )

        return float(score.item())

    # --------------------------------------------------
    # HYBRID SKILL ANALYSIS
    # --------------------------------------------------

    def analyze_skills(
        self,
        candidate_skills,
        required_skills,
        semantic_threshold=0.65
    ):

        exact_matches = []
        semantic_relations = []
        unmatched_skills = []

        for required in required_skills:

            # ------------------------------------------
            # 1. EXACT MATCH
            # ------------------------------------------

            if required in candidate_skills:

                exact_matches.append({
                    "required_skill": required,
                    "matched_skill": required,
                    "similarity": 1.0
                })

                continue

            # ------------------------------------------
            # 2. FIND BEST SEMANTIC MATCH
            # ------------------------------------------

            best_candidate = None
            best_score = 0.0

            for candidate in candidate_skills:

                score = self.similarity(
                    candidate,
                    required
                )

                if score > best_score:
                    best_score = score
                    best_candidate = candidate

            # ------------------------------------------
            # 3. CLASSIFY SEMANTIC RELATION
            # ------------------------------------------

            if best_score >= semantic_threshold:

                semantic_relations.append({
                    "required_skill": required,
                    "related_skill": best_candidate,
                    "similarity": round(best_score, 3)
                })

            else:

                unmatched_skills.append({
                    "required_skill": required,
                    "best_candidate": best_candidate,
                    "similarity": round(best_score, 3)
                })

        return {
            "exact_matches": exact_matches,
            "semantic_relations": semantic_relations,
            "unmatched_skills": unmatched_skills
        }

    # --------------------------------------------------
    # BACKWARD-COMPATIBLE MATCH FUNCTION
    # --------------------------------------------------

    def match_skills(
        self,
        candidate_skills,
        required_skills,
        threshold=0.55
    ):

        matches = []

        for candidate in candidate_skills:

            for required in required_skills:

                score = self.similarity(
                    candidate,
                    required
                )

                if score >= threshold:

                    matches.append({
                        "candidate_skill": candidate,
                        "required_skill": required,
                        "similarity": round(score, 3)
                    })

        return matches


# ------------------------------------------------------
# DIRECT TEST
# ------------------------------------------------------

if __name__ == "__main__":

    matcher = SemanticSkillMatcher()

    candidate_skills = [
        "Python",
        "PyTorch",
        "SQL"
    ]

    required_skills = [
        "Python",
        "Machine Learning",
        "Deep Learning",
        "SQL"
    ]

    analysis = matcher.analyze_skills(
        candidate_skills,
        required_skills
    )

    print("\n==============================")
    print("     HYBRID SEMANTIC TEST")
    print("==============================")

    print("\nEXACT MATCHES:")

    for item in analysis["exact_matches"]:
        print(
            f"{item['matched_skill']} "
            f"→ {item['required_skill']} "
            f"= {item['similarity']}"
        )

    print("\nSEMANTIC RELATIONS:")

    for item in analysis["semantic_relations"]:
        print(
            f"{item['related_skill']} "
            f"→ {item['required_skill']} "
            f"= {item['similarity']}"
        )

    print("\nUNMATCHED / LOW SIMILARITY:")

    for item in analysis["unmatched_skills"]:
        print(
            f"{item['required_skill']} "
            f"← best candidate: {item['best_candidate']} "
            f"= {item['similarity']}"
        )