class Student:
    # [assignment] Skeleton class. Add your code here

    def __init__(self,name,age,tracks,score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score
        pass
    def change_name(self):
        return "Peter"
    def change_age(self):
        return 34
    def add_tracks(self):
        return "UI/UX"
    def get_score():
        return Student.score

Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

