"""
Parts 1-4
Create your classes and class methods here according to the practice instructions.
As you are working on Parts 1, 2, and 4, you can run the test python file
corresponding to that section to verify that you are completing the problem
correctly.
ex: python part_1_tests.py.
"""


class Student(object):
    """Student list and information."""

    def __init__(self, first_name, last_name, address):
        """Initialize with names and address."""
        self.first_name = first_name
        self.last_name = last_name
        self.address = address


class Question(object):
    """Questions and correct answers."""

    def __init__(self, question, correct_answer):
        """Initialize with question and correct answer."""
        self.question = question
        self.correct_answer = correct_answer

    def ask_and_evaluate(self):
        """Prints question, checks user response and returns True or False."""

        # This test correctly for part 2, Exam class, but fails part 4 because 
        # the doctest for Quiz questions expects " " rather than " > " after 
        # the question. Is that intentional, was I supposed to use logic to 
        # modify the raw_input if the question is for a quiz vs exam?
        user_answer = raw_input(self.question + " > ")

        return user_answer == self.correct_answer


class Exam(object):
    """Exams by exam name and question list."""

    def __init__(self, name):
        """Initialize with exam name."""
        self.name = name
        self.questions = []

    def add_question(self, question):
        """Adds a question to an exam's list of questions."""

        self.questions.append(question)

    def administer(self):
        """Gives the exam to user and scores percentage of correct answers."""

        tally = 0.0

        for question in self.questions:
            if question.ask_and_evaluate():
                tally += 1

        number_correct = tally / len(self.questions)

        return number_correct


class Quiz(Exam):
    """A Quiz as a subset of the Exam class."""

    def administer(self):
        """Gives the quiz to user and scores passed(1) or failed(0)."""

        tally = 0.0

        for question in self.questions:
            if question.ask_and_evaluate():
                tally += 1

        number_correct = tally / len(self.questions)

        if number_correct >= .5:
            return 1
        else:
            return 0


class StudentExam(object):
    """Students, their exams taken, and their scores."""

    def __init__(self, student, exam, score=None):
        """Initialize with exam and score."""

        self.student = student
        self.exam = exam
        self.score = score

    def take_test(self, exam):
        """Gives exam to student. Updates self.score, and prints, the result."""

        self.score = exam.administer()

        print "Exam complete, you scored {:-2f}%.".format(self.score * 100)


class StudentQuiz(StudentExam):
    """Students, their quizzes taken, and their scores."""

    def take_test(self, quiz):
        """Gives exam to student. Updates self.score, and prints, the result."""

        self.score = quiz.administer()


def example():
    exam_1 = Exam("exam_1")
    q_1 = Question("Am I blue?", "You'd be too.")
    q_2 = Question("If your plan with your man?", "Done fell through.")
    q_3 = Question("Was a time?", "I was his only one.")
    exam_1.add_question(q_1)
    exam_1.add_question(q_2)
    exam_1.add_question(q_3)
    jane = Student("Jane", "Doe", "123 Anywhere Drive, City, State, Zip")

    jane_testing = StudentExam(jane, exam_1)

    jane_testing.take_test(exam_1)
