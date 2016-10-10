""" Class Student """

class Student(object):
    """Create a Student

       attributes: first_name, last_name, address
    """

    def __init__(self, first_name, last_name, address):
        """Initialize with parameters first_name, last_name, adress"""
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

class Question(object):
    """Create a Question

       attributes: question, correct_answer
       methods: ask_and_evaluate()
    """
    def __init__(self, question, correct_answer):
        """Initialize with parameters question and correct_answer"""
        self.question = question
        self.correct_answer = correct_answer

    def ask_and_evaluate(self):
        """Prompts user for answer, returns boolean

        Prints question, prompts user for answer, returns boolean whether 
        answer is correct or not.
        """
        user_answer = raw_input('{} > '.format(self.question))

        return user_answer == self.correct_answer

class Exam(object):
    """Create an Exam

       attributes: name, list of questions
       methods: add_question(), administer()
    """

    def __init__(self, name):
        """Initialize with parameters name, list of questions"""
        self.name = name
        self.questions = []

    def add_question(self, question, answer):
        """Add question to exam

        Takes in a question and answer, creates an instance of the Question
        class and appends the Question object the the Exam's questions list.
        """
        new_question = Question(question, answer)
        self.questions.append(new_question)

    def administer(self):
        """Administer test, returns score.

        For each quesiton in quesiton list, prints question and prompts user
        for answer. Returns score as a percentage.
        """
        correct = 0.0
        for question in self.questions:
            if question.ask_and_evaluate():
                correct += 1.0
        # score is a percentage
        score = (correct / len(self.questions))
        return score

class Quiz(Exam):
    """Create a Quiz -- subclass of the Exam Class

       Initialzed by parent class.
       attributes: name, list of questions (from parent Exam)
       parent methods: add_question()
       methods: administer()
    """
    def administer(self):
        """Administer test, return boolean whether passed.

        Calls parent's administer() method to receive score percentage,
        returns a boolean of whether the student passeed 
        (>= 50 percent correct answers)
        """
        score = super(Quiz, self).administer()
        return score >= 0.5

def take_test(test, student):
    """administers test

    Takes in an instance of the Exam or Quiz and Student Class, and calls the
    adminster method to prompt user to take test.
    """
    student.score = test.administer()

def example():
    """Example Exam"""
    exam = Exam('Example')
    exam.add_question("What is the capital of CA?", 'Sacramento')
    exam.add_question("What is the capital of NV?", 'Carson City')
    exam.add_question("What is the capital of OR?", 'Salem')
    exam.add_question("What is the capital of WA?", 'Olympia')
    student = Student('Maddie', 'Cousens', 'Berkely, CA')
    take_test(exam, student)
    print "Score: ", student.score

if __name__ == '__main__':
    example()
