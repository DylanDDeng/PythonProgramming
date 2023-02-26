class students: 
    # 构造方法 
    def __init__(self,name,exam_results): 
        self.name = name  
        self.exam_results = exam_results

    # 实例化 
    def study(self): 
    #   self.examination_results  =examination_results 
        print("同学的姓名是{},考试分数为{}".format(self.name, self.exam_results))  
    #   print("该实例对象的地址是{}".format(self))   
    #    return self.name, self.exam_results

    def grade(self, average_grade): 
        self.average_grade = average_grade 
        if (self.exam_results - self.average_grade) > 20 and self.exam_results > 85: 
            return "A" 
        elif (self.exam_results - self.average_grade) < 20 and self.exam_results < 85: 
            return "B" 
        else: 
            return "C"   

# 继承 students 类  
class Parents(students): 
    def __init__(self,name,exam_results,job): 
        # 继承 students的属性 
        super(Parents,self).__init__(name,exam_results)  
        # 新增parents 的属性
        self.job = job

    def getJob(self): 
        print("同学的姓名是{},父母的职业是{}".format(self.name, self.job))


# ----------------------------------------------------------------
#student_a = students("student_a",80) 
#student_a.study()
student_a = students("student_a",80) 
student_a.grade(45)
student_a.study() 

# 继承students 类 
parents_a = Parents("student_a", 80,"doctors") 
parents_a.getJob()
