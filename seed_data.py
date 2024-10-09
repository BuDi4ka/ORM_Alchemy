import random
from faker import Faker
from connection import connect_to_database
from models import Group, Teacher, Subject, Student, Grade

STUDENTS = 50
TEACHERS = 5
SUBJECTS = 8
GROUPS = 3
GRADES = 20

fake = Faker()

def seed_data():
    session = connect_to_database()
    db = session()
    try:
        groups = create_groups(db)
        teachers = create_teachers(db)
        subjects = create_subjects(db, teachers)
        students = create_students(db, groups)
        create_grades(db, students, subjects)
        db.commit()
    except Exception as e:
        print(f"Error occurred: {e}")
        db.rollback()
    finally:
        db.close()

def create_groups(db):
    groups = []
    for _ in range(GROUPS):
        group = Group(name=fake.word().capitalize())
        db.add(group)
        db.flush()
        groups.append(group)
        print(f"Group created: {group.id}, Name: {group.name}")
    return groups

def create_teachers(db):
    teachers = []
    for _ in range(TEACHERS):
        teacher = Teacher(name=fake.name())
        db.add(teacher)
        db.flush()
        teachers.append(teacher)
        print(f"Teacher created: {teacher.id}, Name: {teacher.name}")
    return teachers

def create_subjects(db, teachers):
    if not teachers:
        raise ValueError("No teachers available to assign subjects to.")

    subjects = []
    for _ in range(SUBJECTS):
        teacher = random.choice(teachers)
        subject = Subject(
            name=fake.word().capitalize(),
            teacher_id=teacher.id
        )
        db.add(subject)
        db.flush()
        subjects.append(subject)
        print(f"Subject created: {subject.id}, Name: {subject.name}, Teacher ID: {subject.teacher_id}")

    return subjects

def create_students(db, groups):
    if not groups:
        raise ValueError("No groups available to assign students to.")

    students = []
    for _ in range(STUDENTS):
        group = random.choice(groups)
        student = Student(
            name=fake.name(),
            group_id=group.id
        )
        db.add(student)
        db.flush()
        students.append(student)
        print(f"Student created: {student.id}, Name: {student.name}, Group ID: {student.group_id}")

    return students

def create_grades(db, students, subjects):
    if not students:
        raise ValueError("No students available to assign grades to.")
    if not subjects:
        raise ValueError("No subjects available to assign grades to.")

    for student in students:
        for _ in range(random.randint(1, GRADES)):
            subject = random.choice(subjects)
            grade = Grade(
                student_id=student.id,
                subject_id=subject.id,
                grade=random.randint(1, 12)
            )
            db.add(grade)
            print(f"Grade created: Student ID: {student.id}, Subject ID: {subject.id}, Grade: {grade.grade}")

