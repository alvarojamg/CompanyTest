

class CalculateService:
    
    numbers = list(range(1,101))
    numbres_extracted = []

    def extract_number(self, number):
        
        if number > 100:
            return "Error, number out of range"
        
        if not isinstance(number,int) or number<= 0:
            return "Error, number isnt natural"
        
        if number not in self.numbers:
            return f"The number : {number}, was extracted"
        
        self.numbers.remove(number)
        
        print(self.numbers)
        self.numbres_extracted.append(number)
        
        return f"Number extracted: {number}"


    def calculate_number_extracted(self):
        
        if len(self.numbres_extracted) > 1:
            
            return {"numbers_extracted": self.numbres_extracted }
            
        total = 100 * 101 // 2
        print("total",total)
        
        print(self.numbers)
        total_actual = sum(self.numbers)
        
        print(total_actual)
        
        return total - total_actual
