def run_quiz():
    # List of questions with options and correct answers
    questions = [
        {
            "question": "What is the keyword to define a function in Python?",
            "options": ["A. func", "B. def", "C. function", "D. define"],
            "answer": "B"
        },
        {
            "question": "Which movie won the Oscar for Best Picture in 2022?",
            "options": ["A. CODA", "B. Dune", "C. The Power of the Dog", "D. West Side Story"],
            "answer": "A"
        },
        {
            "question": "What is the capital of France?",
            "options": ["A. Madrid", "B. Rome", "C. Paris", "D. Berlin"],
            "answer": "C"
        },
        {
            "question": "Which animal is known as the 'King of the Jungle'?",
            "options": ["A. Tiger", "B. Elephant", "C. Lion", "D. Gorilla"],
            "answer": "C"
        },
        {
            "question": "Who wrote 'Harry Potter'?",
            "options": ["A. J.R.R. Tolkien", "B. George R.R. Martin", "C. J.K. Rowling", "D. Stephen King"],
            "answer": "C"
        }
    ]
    
    score = 0  # Initialize the score
    
    # Loop through each question
    for i, q in enumerate(questions, start=1):
        print(f"\nQuestion {i}: {q['question']}")
        for option in q["options"]:
            print(option)
        
        # Get user's answer and validate it
        user_answer = input("Enter your answer (A, B, C, or D): ").strip().upper()
        
        # Check if answer is correct
        if user_answer == q["answer"]:
            print("Correct! 🎉")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['answer']}.")
    
    # Display final score
    print(f"\nYour final score: {score} out of {len(questions)}")
    
    # Play again option
    play_again = input("Do you want to play again? (yes or no): ").strip().lower()
    if play_again == "yes":
        run_quiz()
    else:
        print("Thanks for playing! 🏆")

# Run the quiz
run_quiz()
