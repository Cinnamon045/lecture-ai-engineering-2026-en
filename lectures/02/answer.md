# Lecture 02 Answers

## Exercises

- Model and settings used (from `config` in `result.json`):
- Did you run training yourself (`executed_training_myself`): Yes / No (how far you ran the notebook: )
- Before training: `format_rate` = / `content_rate` =
- After training: `format_rate` = / `content_rate` =
- Questions that regressed:
- Failures remaining after training and their types (assertion without evidence / evasion through a confirmation request despite evidence being present / broken format):
- Results of knowledge questions (section 6; classification before → after training) and observations:
- What changed and what stayed the same with training:

## Homework

- Level attempted: Basic / Implementation / Advanced

    Implementation

- Settings or data changed:

    I changed this code questions:

    FAQ = {
    "deadline": "The assignment deadline is September 30 at 23:59 (Japan time).",
    "destination": "Submit through the 'Assignments' section of the learning portal.",
    "format": "Submit one PDF file named student_id_assignment_number.pdf.",
    "office_hours": "Questions are welcome during office hours every Tuesday from 17:00 to 18:00.",
    "late": "Late submissions are accepted within 48 hours of the deadline, with a grade penalty.",
}
FAQ_TEXT = "\n".join(f"- {v}" for v in FAQ.values())

# With evidence: (FAQ key, question templates, required keywords in the expected answer)
GROUNDED = {
    "deadline": (["When is the assignment deadline?", "By when should I submit?", "Tell me the deadline", "What is the submission deadline?"], ["September 30", "23:59"]),
    "destination": (["Where should I submit?", "Where do I upload it?", "Where can I submit the assignment?", "Where should I submit my work?"], ["learning portal", "Assignments"]),
    "format": (["Tell me the submission format", "Are there any file naming rules?", "Which file format should I submit?", "Can I submit a format other than PDF?"], ["PDF"]),
    "office_hours": (["When can I ask questions?", "When are office hours?", "Is there a time to ask the instructor questions?", "What times are available for consultation?"], ["Tuesday", "17:00"]),
    "late": (["What happens if I submit late?", "Are submissions accepted after the deadline?", "What are the late submission rules?", "Tell me how submissions after the deadline are handled"], ["48 hours", "penalty"]),
}
# Without evidence: absent from the FAQ, so needs_review=true is correct
UNGROUNDED = [
    "Can I resubmit?", "Tell me how missed lectures are handled", "Can I see other participants' scores?",
    "When will grades be released?", "Can the submission deadline be extended?", "Are group submissions allowed?",
    "How are points allocated for assignments?", "Will lecture recordings be made available?",
]

# Additional test-only questions (excluded from train / valid)
TEST_EXTRA_GROUNDED = {
    "deadline": ["Tell me the submission deadline date and time", "On what date and at what time is the assignment due?"],
    "destination": ["Where do I hand in the assignment?", "Tell me where to send my submission"],
    "format": ["What format should the submitted file use?", "What file format and how many files should I submit?"],
    "office_hours": ["Tell me the day and time of office hours", "On which day and from what time can I ask questions?"],
    "late": ["What happens if I miss the submission deadline?", "Will an assignment submitted after the deadline be accepted?"],
}
TEST_EXTRA_UNGROUNDED = [
    "Is there a character count limit for assignments?", "Will I receive feedback on my submitted assignment?",
    "Is a particular citation style required?", "Do office hours require an appointment?",
]
UNGROUNDED_ANSWER = "This FAQ does not contain that information. Confirmation from the course organizers is needed."

    Into this "Grounded Questions":

    #This is the new content
FAQ = {
    "hours": "The library is open Monday to Saturday from 8:00 to 20:00 and is closed on Sundays.",
    "borrowing": "Students may borrow up to 5 books at a time for a loan period of 14 days.",
    "renewal": "Loans can be renewed twice online through your library account, unless another patron has reserved the book.",
    "fines": "Overdue books are charged a fine of 10 pesos per day per book.",
    "printing": "Printing is available at the second-floor service desk at 2 pesos per page.",
}
FAQ_TEXT = "\n".join(f"- {v}" for v in FAQ.values())

# With evidence: (FAQ key, question templates, required keywords in the expected answer)
GROUNDED = {
    "hours": (["What are the library opening hours?", "When does the library open?", "Is the library open on Sundays?", "What time does the library close?"], ["8:00", "20:00"]),
    "borrowing": (["How many books can I borrow?", "How long can I keep a borrowed book?", "What is the loan period?", "What are the borrowing limits for students?"], ["5 books", "14 days"]),
    "renewal": (["Can I renew a book?", "How do I renew my loan?", "How many times can I extend a loan?", "Can I renew books online?"], ["twice", "online"]),
    "fines": (["How much is the overdue fine?", "What happens if I return a book late?", "Are there penalties for late returns?", "How are overdue books charged?"], ["10 pesos", "per day"]),
    "printing": (["Where can I print documents?", "How much does printing cost?", "Is printing available in the library?", "What is the price per printed page?"], ["second-floor", "2 pesos"]),
}
# Without evidence: absent from the FAQ, so needs_review=true is correct
UNGROUNDED = [
    "Can I reserve a study room?", "Does the library have free Wi-Fi?", "Can I borrow a laptop?",
    "How do I request an interlibrary loan?", "Are guests allowed inside the library?", "Can I bring food and drinks?",
    "Is there a membership fee for alumni?", "How do I donate books to the library?",
]

# Additional test-only questions (excluded from train / valid)
TEST_EXTRA_GROUNDED = {
    "hours": ["Tell me the days and times the library is open", "From what time until what time can I visit the library?"],
    "borrowing": ["How many books can I take out and for how long?", "Tell me the maximum number of books and the loan duration"],
    "renewal": ["Is it possible to extend my loan, and how?", "How many renewals are allowed for a borrowed book?"],
    "fines": ["What is the daily charge for an overdue book?", "How much will I pay if my book is late by several days?"],
    "printing": ["Where is the printing service and what does it cost?", "Tell me the location and price of printing"],
}
TEST_EXTRA_UNGROUNDED = [
    "Is there a quiet floor for studying?", "Can I scan documents for free?",
    "Do I need a student ID to enter?", "Are there extended hours during exam week?",
]
UNGROUNDED_ANSWER = "This FAQ does not contain that information. Confirmation from the library staff is needed."

- Results (comparison tables or numbers):

    By changing the grounded questions, the model were able to answer the questions that I included. Those questions that was not included was therefore not answerable by the model. 

- Discussion of when fine-tuning is and is not suitable:

    Fine-tuning suits teaching behavior and format: a fixed JSON answer, a consistent tone, or saying “confirmation is needed” when the FAQ is silent. It works when the facts stay in the prompt, so changing a deadline needs no retraining, and when questions are narrow and stable. It is unsuitable when facts change often, because they go stale in the weights and force retraining. It also fails with many questions, when answers need sources, and when the model must judge whether evidence exists. Your tuned model copied the nearest FAQ item instead of abstaining. 