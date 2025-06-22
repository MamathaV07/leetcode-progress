class Solution:
    def average(self, salary: List[int]) -> float:
        new_salary = []

        minimum = min(salary)
        maximum = max(salary)
        
        for i in salary:
            if i !=minimum and i!=maximum:
                new_salary.append(int(i))
        avg = sum(new_salary) / len(new_salary)
        return avg
        