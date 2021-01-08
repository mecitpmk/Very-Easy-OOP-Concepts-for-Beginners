

class User:
    total_user = 0
    users_lists = []
    def __init__(self,id,password,budget):
        self.id = id
        self.password = password
        self.budget = budget
        self.registered_courses_list = []
        self.registered_courses_dict = {}
        
        User.total_user+=1
        User.users_lists.append(self)
    
    def displayInfo(self):
        print(f'ID = {self.id}')
        print(f'Budget = {self.budget}')
        if len(self.registered_courses_list) > 0:
            for courses in self.registered_courses_list:
                print(f'Course name = {courses.name} , Credit = {courses.credit}')
        else:
            print("No Registered Courses")

    def canTakeCourse(self,course_obj):
        if course_obj.credit*100 <= self.budget and course_obj not in self.registered_courses_list:
            return True
        return False
    
    def deleteCoursefromTakenCourse(self,course_obj,drop_specific=False):
        self.budget += course_obj.credit*100
        self.registered_courses_list.remove(course_obj)
        if drop_specific:
            course_obj.registered_users.remove(self)

    def deleteUser(self):
        for taken_courses in self.registered_courses_list:
            taken_courses.registered_users.remove(self)
        User.users_lists.remove(self)
    def takeCourse(self,course_obj):
        
        self.budget -= course_obj.credit*100
        self.registered_courses_list.append(course_obj)
        course_obj.registered_courses.append(self)

    def dropAllCourses(self):
        for courses in self.registered_courses_list:
            self.budget += courses.credit*100
            courses.registered_users.remove(self)
        
    def __repr__(self):
        return self.id

class Course:
    total_courses = 0
    courses_lists = []
    def __init__(self,name,credit):
        self.name = name
        self.credit = credit
        self.registered_users = []

        Course.total_courses += 1
        Course.courses_lists.append(self)

    def removeCourse(self):
        for users in self.registered_users:
            users.deleteCoursefromTakenCourse(self)
            self.registered_users.remove(users)
        Course.courses_lists.remove(self)
    
    def removeUserfromCourse(self,user_obj):
        user_obj.deleteCoursefromTakenCourse(self)
        self.registered_users.remove(user_obj)
    
    
    def __repr__(self):
        return f'Name : {self.name} - Credit : {self.credit}'

class System:
    def __init__(self):
        self.login_infos = {"admin":123}
        
        
        self.offered_courses = Course.courses_lists
        self.all_users = User.users_lists


    def UserBudgets(self):
        user_budgets = {}
        for user in self.all_users:
            user_budgets[user] = user.budget
        return user_budgets


    def showAllUsers(self):
        for user in self.all_users:
            user.displayInfo()
    
    def deleteSpecificUser(self,user_obj):
        user_obj.deleteUser()

    def deleteSpecificCourses(self,course_obj):
        course_obj.removeCourse()
    
    def droppSpecificLesson(self,user,course_obj):
        user.deleteCoursefromTakenCourse(course_obj,drop_specific=True)
    
    def dropUserfromLesson(self,course,user):
        course.removeUserfromCourse(user)

    def createUser(self,id,password,budget):
        self.login_infos[id] = password
        return User(id,password,budget)
    
    def createCourse(self,name,credit):
        return Course(name,credit)
    
    def showAllCourses(self):
        for counter,courses in enumerate(self.offered_courses):
            print(f'{counter+1} - {courses}')
    
    def showCantakeCoursesforUser(self,user_obj):
        can_take_courses = []
        for courses in self.offered_courses:
            if (user_obj.canTakeCourse(courses)):
                can_take_courses.append(courses)
        return can_take_courses
    

    
