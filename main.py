class Student():
  def __init__(self, name, score):
    self.name = name
    self.score = score
    
def main():
    students = get_records()
    find_cutoff(students)
    
def get_records():
  records = []
  
  file = open('data_in.csv')
  
  for line in file:
     data = line.replace('"','').strip().split(",")
    
     name = data[0]
     score = int(data[1])
    
     records.append(Student(name, score))
    
  return records
  
  file.close()
  
  
def find_cutoff(records):
  
    cutoff = int(input('What is the cutoff score? '))
    print()
    for x in range(len(records)):
      if records[x].score >= cutoff:
       print(records[x].name, records[x].score)
    

main()