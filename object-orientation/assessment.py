"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

   - Abstraction: abstraction is the ability to use a function/method without
        knowing how it works. It is the practice of hiding the interworkings of 
        a method and making very clear only what the user neads: functionality, 
        inputs, outputs. Object orientation creates and easy interface between
        writer and user of the code.

   - Polymorphism: Polymorphism is the notion of having interchangable components.
        Specifically, the ability to retreive data and call methods in a standardized
        way across all instances of a Class (and subclasses).

   - Encapsulation: Encapsulation is the idea of having all data living closely
        to it's functionality. In practice this means having all data and methods
        specific to an object live withint the object class.

2. What is a class?
    A class is a created data structure. It is a way to store data (attributes)
    and define functions (methods) that can be used on the object. 

3. What is an instance attribute?
    An instance attribute is a piece of data specific to an instance of a class.

4. What is a method?
    A method is a function defined within a class and used by instances of a
    class. It always takes 'self' as a first parameter.

5. What is an instance in object orientation?
    An instance is a specific implementation of a Class. It can also be called
    a class object. You can create multiple instances of a class and assign
    different attributes to them.

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

   A class attribute is a piece of data that every instance of the class can use.
   Example: every instance of a Cat class could have a class attribute of having 
   a tail.

   An instance attribute is a piece of data specific to a instance of a class.
   Example: every instance of a Cat class has a different name.



"""

# Create your classes and class methods

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